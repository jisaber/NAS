import os
FILR_TYPE_ERROR = -1
FILR_TYPE_VIDEO = 0
FILR_TYPE_AUDIO = 1
FILR_TYPE_IMAGE = 2

def human_size(size):
    if size < 1024:
        return str(size) + " Byte"
    elif size < 1024 * 1024:
        return str(round(size / 1024, 2)) + " Kb"
    elif size < 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024), 2)) + " Mb"
    elif size < 1024 * 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024 * 1024), 2)) + " Gb"
    elif size < 1024 * 1024 * 1024 * 1024 * 1024:
        return str(round(size / (1024 * 1024 * 1024 * 1024), 2)) + " Tb"
    elif size < 1024 * 1024 * 1024 * 1024 * 1024 *1024:
        return str(round(size / (1024 * 1024 * 1024 * 1024 *1024), 2)) + " Pb"

def get_file_type(filename):
    video_extensions = ('mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'webm')
    audio_extensions = ('mp3')
    image_extensions = ('jpg', 'jpeg', 'png')
    if filename.lower().endswith(video_extensions):
        return FILR_TYPE_VIDEO
    elif filename.lower().endswith(audio_extensions):
        return FILR_TYPE_AUDIO
    elif filename.lower().endswith(image_extensions):
        return FILR_TYPE_IMAGE
    else:
        return FILR_TYPE_ERROR