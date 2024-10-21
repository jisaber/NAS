import os

def is_video_file(filename):
    video_extensions = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm')
    return filename.lower().endswith(video_extensions)
 