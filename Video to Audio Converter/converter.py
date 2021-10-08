# importing moviepy editor from moviepy
from moviepy.editor import *

# asking for the video file along with its extension
video_file =  input("Enter path of file (including extension):")
# asking for the audio file name along without its extension
audio_file =  input("Enter name of audio file (without extension):")
# asking for the folder name where do you wanna save file
path = input("Enter path of folder where you wanna save audio file:")

# clip vedio to the video file clip in editor
# it's like adding file into any video editor
clip  = VideoFileClip(video_file)

# set clip audio to the variable audio
audio = clip.audio

# write audio where the path is given and with tha name given with extension .mp3
audio.write_audiofile(path+audio_file+".mp3")

# closing the clip ... Removing clip from video editor
clip.close()
# closing that audio too
audio.close()