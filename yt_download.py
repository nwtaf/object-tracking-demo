import os
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Specify the YouTube URL
youtube_url = 'https://youtu.be/FCBJ1C6_hig?si=KhKqOrsjum6efpZa'

# Create a YouTube object
yt = YouTube(youtube_url)

# Specify the relative path to the data directory
data_dir = os.path.join(os.getcwd(), 'data')

# Download the highest quality video to the data directory
download_path = yt.streams.get_highest_resolution().download(data_dir)

# # Get the name of the YouTube video
# video_name = yt.title

# # Replace invalid characters
# video_name = video_name.replace("|", "-").replace(":", "-")

# Specify the output file for the segment using the video name
output_file = os.path.join(data_dir, f'hike.mp4')

# Specify the start and end times of the segment you want to save (in seconds)
start_time = 122
end_time = 125

# Extract the segment and save it with the specified frame rate
ffmpeg_extract_subclip(download_path, start_time, end_time, targetname=output_file)

'''
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

download_path = 'data/rpi_overclock_failure.mp4'
start_time = 0
end_time = 100
output_file = 'data/rpi_overclock_failure_segment.mp4'
frame_rate = 60

# Set the desired frame rate (e.g., 30 fps or 60 fps)
frame_rate = 60  # Change to desired frame rate

# Command to extract subclip with specified frame rate using ffmpeg
ffmpeg_command = f"ffmpeg -i {download_path} -r {frame_rate} -ss {start_time} -to {end_time} {output_file}"

# Execute the command
os.system(ffmpeg_command)
'''