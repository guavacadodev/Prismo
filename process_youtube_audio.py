import yt_dlp as youtube_dl
from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import logging

# Configure logging
logging.basicConfig(filename='video_processing.log', level=logging.DEBUG)

# Explicitly set the path to FFmpeg
AudioSegment.ffmpeg = "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"

def download_and_extract_audio(video_url, output_dir='output'):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        # Define ydl_opts for audio extraction
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }

        # Download video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        # Find the downloaded file
        for file_name in os.listdir(output_dir):
            if file_name.endswith('.wav'):
                audio_file = os.path.join(output_dir, file_name)
                print(f"Extracted audio to: {audio_file}")
                return audio_file

    except Exception as e:
        logging.error(f"Failed to download and extract audio for {video_url}: {e}")
        print(f"Error in download_and_extract_audio: {e}")
        return None

def segment_audio(file_path, output_dir='output', chunk_length_ms=10000):
    try:
        audio = AudioSegment.from_wav(file_path)
        chunks = make_chunks(audio, chunk_length_ms)

        chunk_files = []
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        for i, chunk in enumerate(chunks):
            chunk_name = os.path.join(output_dir, f"{base_name}_chunk{i}.wav")
            print(f"Exporting chunk to: {chunk_name}")
            chunk.export(chunk_name, format="wav")
            chunk_files.append(chunk_name)

        return chunk_files
    except Exception as e:
        logging.error(f"Failed to segment audio for {file_path}: {e}")
        print(f"Error in segment_audio: {e}")
        return []

def process_videos(video_urls, output_dir='output'):
    all_chunk_files = []
    for url in video_urls:
        try:
            audio_file = download_and_extract_audio(url, output_dir)
            if audio_file:
                chunk_files = segment_audio(audio_file, output_dir)
                all_chunk_files.extend(chunk_files)
            else:
                print(f"Audio file not created for {url}")
        except Exception as e:
            logging.error(f"Failed to process {url}: {e}")
            print(f"Error in process_videos for URL {url}: {e}")

    return all_chunk_files

# List of YouTube video URLs
video_urls = [
    "https://www.youtube.com/watch?v=ekxd7QMuvHE",
    "https://www.youtube.com/watch?v=BzkOM14Tnww",
    "https://www.youtube.com/watch?v=ZbVFr0-CFCg"
]

# Process all videos
all_chunk_files = process_videos(video_urls)

print("All audio chunks have been created.")

