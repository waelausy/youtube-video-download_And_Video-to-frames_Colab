# Youtube video download and Video to frames

This repo contains two codes:
- Download youtube video using the python library [pytube](https://buildmedia.readthedocs.org/media/pdf/python-pytube/latest/python-pytube.pdf) **video_yt_pytube_download.py**.
- Extract frames from video using the parameter **frame_every** allowing the definition of the distance between two saved frames (for example if we set **frame_every = 500**, the program will save one image each 500 frames.


### video_yt_pytube_download.py

python3 video_yt_pytube_download.py --video **https://www.youtube.com/XXXX** --resolution **720p**

### video_to_frames.py

python3 video_to_frames .py -video **VIDEO.mp4** -frame_every **500**