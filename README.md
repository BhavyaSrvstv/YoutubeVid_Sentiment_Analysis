# YouTube Sentiment Analysis with Speech Recognition

This project aims to provide both transcription and sentiment analysis for audio content using AssemblyAI's speech recognition API. In this specific implementation, we used a YouTube video (iPhone 13 review) as a sample. The process involves extracting the audio URL from the YouTube video, downloading the audio in the M4A format, converting it to MP3, and finally uploading the MP3 file for transcription and sentiment analysis.

## Usage

1. Run `yt_extractor.py` to extract the audio URL from the specified YouTube video.
2. Download the audio in MP3 format and provide the file path in the `filename` variable in the provided script.
3. Execute the script to transcribe the audio and perform sentiment analysis.
