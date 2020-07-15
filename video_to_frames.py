# Use example
# python3 video_to_frames .py -video VIDEO.mp4 -frame_every 500
# Program To Read video 
# and Extract Frames 

import cv2
import os, sys
import argparse

parser = argparse.ArgumentParser()
ap = argparse.ArgumentParser()
ap.add_argument("-v","--video", type=str, help="path to the video to cut")
ap.add_argument("-f","--frame_every", type=int, default=500, help="the program will save one image every XXX frames")
args = ap.parse_args()


# Path to be created
path  = "Frames"

try:
    os.mkdir(path)
    print("Path is created")
except:
    print("Path exists already")
    pass


# Function to extract frames 
def FrameCapture(path): 
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
    fps_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))
    print('Number of frames in the video',fps_count,'\nNumber of saved images',1+int(fps_count/args.frame_every))
    # Used as counter variable 
    count = 0
    # checks whether frames were extracted 
    success = 1
    while success: 
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        # Saves the frames with frame-count 
        if count % args.frame_every == 0:
            cv2.imwrite("Frames/frame%d.jpg" % count, image)
        count += 1

# Driver Code 
if __name__ == '__main__': 
    # Calling the function 
    FrameCapture(args.video) 
    print('\nEnd of the program')
