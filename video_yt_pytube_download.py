### Example use 
### python3 video_yt_pytube_download.py --video https://www.youtube.com/watch?v=iQhpFTiFgIY --resolution 720p
### Wael BEN MESSAOUD github waelausy

from pytube import YouTube

import argparse

# construct the argument parser and parse the arguments

parser = argparse.ArgumentParser()
ap = argparse.ArgumentParser()
ap.add_argument("-v","--video", type=str, help="path to the youtube video")
ap.add_argument("-r","--resolution", type=str, default="720p", help="resolution of the output video '360p' '480p' '720p'....")

args = ap.parse_args()

#YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
video = YouTube(args.video)
print('Start downloading video:',video.streams[0].default_filename,'[',args.video,']')
#video.streams.all()
#video.streams.get_by_itag(136).download()
video.streams.get_by_resolution(args.resolution).download()

print('Video',video.streams[0].default_filename,'resolution',args.resolution,'downloaded...')