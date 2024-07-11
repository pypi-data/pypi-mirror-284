## usage examples
```python
from RTPSender import RTPSender

rtpSender = RTPSender("127.0.0.1", 7777)
rtpSender.send_video_rtp("image.png")
rtpSender.send_audio_rtp("audio.wav")
```