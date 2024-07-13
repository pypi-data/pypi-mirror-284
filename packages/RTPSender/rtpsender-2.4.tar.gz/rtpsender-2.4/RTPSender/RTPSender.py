from scapy.all import IP, UDP, Raw, send
import cv2
import av
from pydub import AudioSegment
import queue
import threading
import ctypes


class RTPSender:
    def __init__(self, ip_address, port):
        self.image_queue = queue.Queue()
        self.audio_queue = queue.Queue()
        self.image_queue2 = queue.Queue()
        self.audio_queue2 = queue.Queue()
        self.image_file = ""
        self.audio_file = ""
        self.ip_address = ip_address
        self.port = port
        self.output_path = 'output.mp4'

        # 默认video RTP header参数
        self.RTP_VERSION = 2
        self.RTP_PAYLOAD_TYPE = 96
        self.RTP_SEQUENCE_NUMBER = 0
        self.RTP_TIMESTAMP = 0
        self.RTP_SSRC = 12345

        # 默认音频 RTP header 参数
        self.RTP_AUDIO_VERSION = 2
        self.RTP_AUDIO_PAYLOAD_TYPE = 97
        self.RTP_AUDIO_SEQUENCE_NUMBER = 0
        self.RTP_AUDIO_TIMESTAMP = 0
        self.RTP_AUDIO_SSRC = 12345

        self.max_payload_size = 1400

        # 初始化输出容器
        self.output_container = av.open(self.output_path, mode='w')

        # 创建视频流
        self.video_stream = self.output_container.add_stream('libx264', rate=25)

        self.video_stream.options = {'g': str(25)}  # 设置GOP大小为12
        self.video_stream.bit_rate = 1000000
        # self.video_stream.width = frame_size[0]
        # self.video_stream.height = frame_size[1]

        self.video_stream.width = 1080
        self.video_stream.height = 1920

        self.video_thread = threading.Thread(target=self.process_video_queue)
        self.video_thread2 = threading.Thread(target=self.process_video_queue2)
        self.audio_thread = threading.Thread(target=self.process_audio_queue)
        self.audio_thread2 = threading.Thread(target=self.process_audio_queue2)

        self.video_thread.start()
        self.video_thread2.start()
        self.audio_thread.start()
        self.audio_thread2.start()

    def create_rtp_packet(self, payload):
        rtp_header = bytearray(12)

        # 设置 RTP Header
        rtp_header[0] = (self.RTP_VERSION << 6)
        rtp_header[1] = self.RTP_PAYLOAD_TYPE
        rtp_header[2] = (self.RTP_SEQUENCE_NUMBER >> 8) & 0xFF
        rtp_header[3] = self.RTP_SEQUENCE_NUMBER & 0xFF
        rtp_header[4] = (self.RTP_TIMESTAMP >> 24) & 0xFF
        rtp_header[5] = (self.RTP_TIMESTAMP >> 16) & 0xFF
        rtp_header[6] = (self.RTP_TIMESTAMP >> 8) & 0xFF
        rtp_header[7] = self.RTP_TIMESTAMP & 0xFF
        rtp_header[8] = (self.RTP_SSRC >> 24) & 0xFF
        rtp_header[9] = (self.RTP_SSRC >> 16) & 0xFF
        rtp_header[10] = (self.RTP_SSRC >> 8) & 0xFF
        rtp_header[11] = self.RTP_SSRC & 0xFF
        
        return rtp_header + payload
    
    def create_audio_rtp_packet(self, payload):
        rtp_header = bytearray(12)

        # 设置 RTP Header
        rtp_header[0] = (self.RTP_AUDIO_VERSION << 6)
        rtp_header[1] = self.RTP_AUDIO_PAYLOAD_TYPE
        rtp_header[2] = (self.RTP_AUDIO_SEQUENCE_NUMBER >> 8) & 0xFF
        rtp_header[3] = self.RTP_AUDIO_SEQUENCE_NUMBER & 0xFF
        rtp_header[4] = (self.RTP_AUDIO_TIMESTAMP >> 24) & 0xFF
        rtp_header[5] = (self.RTP_AUDIO_TIMESTAMP >> 16) & 0xFF
        rtp_header[6] = (self.RTP_AUDIO_TIMESTAMP >> 8) & 0xFF
        rtp_header[7] = self.RTP_AUDIO_TIMESTAMP & 0xFF
        rtp_header[8] = (self.RTP_AUDIO_SSRC >> 24) & 0xFF
        rtp_header[9] = (self.RTP_AUDIO_SSRC >> 16) & 0xFF
        rtp_header[10] = (self.RTP_AUDIO_SSRC >> 8) & 0xFF
        rtp_header[11] = self.RTP_AUDIO_SSRC & 0xFF
        
        return rtp_header + payload
    
    def send_video_rtp_from_file(self, image_file, frame_size=(1080, 1920)):        

        img = cv2.imread(image_file)
        img_frame = av.VideoFrame.from_ndarray(img, format='rgb24')
        packets = self.video_stream.encode(img_frame)

        # packets = self.video_stream.encode(None)
        for packet in packets:
            buffer_ptr = packet.buffer_ptr
            buffer_size = packet.buffer_size
            buffer = (ctypes.c_char * buffer_size).from_address(buffer_ptr)

            data = self.video_stream.codec_context.extradata

            import copy
            buffer_copy = copy.deepcopy(buffer)

            self.image_queue.put((buffer_copy, data))


    def process_video_queue(self):
        print("Processing video queue from file")
        while True:
            buffer, data = self.image_queue.get()

            # 初始化输出容器
            # output_container = av.open(self.output_path, mode='w')

            buffer_bytes = bytes(buffer)

            # 要检查的前缀
            begin = b'\x00\x00\x01\x06'
            end = b'\x00\x00\x00\x01\x65'

            # 判断缓冲区是否以指定前缀开头
            if buffer_bytes.startswith(begin):
                pos = buffer_bytes.find(end)
                if pos != -1:                                
                    buffer = data + buffer[pos:]
            elif buffer_bytes.startswith(end):
                buffer = data + buffer

            j = 0
            while j < len(buffer):
                payload = buffer[j:j + self.max_payload_size]
                
                # 创建 RTP 包
                rtp_packet = self.create_rtp_packet(payload)
                
                ip = IP(dst=self.ip_address)
                udp = UDP(dport=self.port)
                raw = Raw(load=rtp_packet)

                packet = ip / udp / raw
                send(packet, verbose=False)
                
                self.RTP_SEQUENCE_NUMBER += 1
                j += self.max_payload_size
                
                # 如果当前负载不足1400字节，说明当前帧处理完了，增加时间戳准备发送下一帧
                if len(payload) < self.max_payload_size:
                    self.RTP_TIMESTAMP += 3000

            # 关闭容器
            # output_container.close()

    def send_audio_rtp_from_file(self, audio_file):
        # print("Received audio file, and put it into queue")
        audio = AudioSegment.from_file(audio_file, format="wav")
        audio_data = audio.raw_data
        # 将音频数据放入队列，等待另一个线程处理
        self.audio_queue.put(audio_data)


    def process_audio_queue(self):
        print("Processing audio queue from file")
        while True:
            audio_data = self.audio_queue.get()

            # 将音频数据分割为1920字节的帧
            i = 0
            while i < len(audio_data):
                frame_data = audio_data[i:i + 1920]
                i += 1920

                j = 0
                while j < len(frame_data):
                    payload = frame_data[j:j + self.max_payload_size]

                    # print(f"Sending audio frame {j} to {j + self.max_payload_size} bytes")

                    # 创建 RTP 包
                    rtp_packet = self.create_audio_rtp_packet(payload)
                    
                    ip = IP(dst=self.ip_address)
                    udp = UDP(dport=self.port)
                    raw = Raw(load=rtp_packet)

                    packet = ip / udp / raw
                    send(packet, verbose=False)
                    
                    self.RTP_AUDIO_SEQUENCE_NUMBER += 1
                    j += self.max_payload_size

                    # 如果当前负载不足1400字节，说明音频流帧处理完了
                    if len(payload) < self.max_payload_size:
                        self.RTP_AUDIO_TIMESTAMP += 3000

            # sleep(0.018)
    
    def send_video_rtp_from_img(self, img, frame_size=(1080, 1920)):

        img_frame = av.VideoFrame.from_ndarray(img, format='rgb24')

        packets = self.video_stream.encode(img_frame)

        data = self.video_stream.codec_context.extradata

        for packet in packets:
            buffer_ptr = packet.buffer_ptr
            buffer_size = packet.buffer_size
            buffer = (ctypes.c_char * buffer_size).from_address(buffer_ptr)

            self.image_queue2.put((buffer, data))


    def process_video_queue2(self):
        print("Processing video queue from img")

        while True:
            buffer, data = self.image_queue2.get()
                
            buffer_bytes = bytes(buffer)

            # 要检查的前缀
            begin = b'\x00\x00\x01\x06'
            end = b'\x00\x00\x00\x01\x65'

            # 判断缓冲区是否以指定前缀开头
            if buffer_bytes.startswith(begin):
                pos = buffer_bytes.find(end)
                if pos != -1:                                
                    buffer = data + buffer[pos:]
            elif buffer_bytes.startswith(end):
                buffer = data + buffer

            j = 0
            while j < len(buffer):
                payload = buffer[j:j + self.max_payload_size]
                
                # 创建 RTP 包
                rtp_packet = self.create_rtp_packet(payload)
                
                ip = IP(dst=self.ip_address)
                udp = UDP(dport=self.port)
                raw = Raw(load=rtp_packet)

                packet = ip / udp / raw
                send(packet, verbose=False)
                
                self.RTP_SEQUENCE_NUMBER += 1
                j += self.max_payload_size
                
                # 如果当前负载不足1400字节，说明当前帧处理完了，增加时间戳准备发送下一帧
                if len(payload) < self.max_payload_size:
                    self.RTP_TIMESTAMP += 3000

        # 关闭容器
        # output_container.close()

    def send_audio_rtp_from_bytes(self, audio_bytes):
        # 将音频数据放入队列，等待另一个线程处理
        self.audio_queue2.put(audio_bytes)


    def process_audio_queue2(self):
        print("Processing audio queue from bytes")

        while True:
            audio_data = self.audio_queue2.get()

            # 将音频数据分割为1920字节的帧
            i = 0
            while i < len(audio_data):
                frame_data = audio_data[i:i + 1920]
                i += 1920

                j = 0
                while j < len(frame_data):
                    payload = frame_data[j:j + self.max_payload_size]

                    # print(f"Sending audio frame {j} to {j + self.max_payload_size} bytes")

                    # 创建 RTP 包
                    rtp_packet = self.create_audio_rtp_packet(payload)
                    
                    ip = IP(dst=self.ip_address)
                    udp = UDP(dport=self.port)
                    raw = Raw(load=rtp_packet)

                    packet = ip / udp / raw
                    send(packet, verbose=False)
                    
                    self.RTP_AUDIO_SEQUENCE_NUMBER += 1
                    j += self.max_payload_size

                    # 如果当前负载不足1400字节，说明音频流处理完了
                    if len(payload) < self.max_payload_size:
                        self.RTP_AUDIO_TIMESTAMP += 3000
