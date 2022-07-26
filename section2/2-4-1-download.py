import os
import subprocess

from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=SvQ9DR-BVuk').streams.first().download()
yt = YouTube("https://www.youtube.com/watch?v=SvQ9DR-BVuk") 

vids= yt.streams.all()


for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Enter the number of the video you want to download: "))

parent_dir = "."
vids[vnum].download(parent_dir) # download the video

new_filename = input("Enter the new filename: ")

default_filename = vids[vnum].default_filename 
subprocess.call(['ffmpeg', '-i',                 #cmd to rename the file
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('Done!')
