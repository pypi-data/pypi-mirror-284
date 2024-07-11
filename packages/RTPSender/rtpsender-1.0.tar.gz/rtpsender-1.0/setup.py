from setuptools import setup, find_packages

setup(
    name="RTPSender",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'scapy',
        'opencv-python',
        'av',
        'pydub'
    ],
    description="A SDK for sending RTP streams",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.9',
)
