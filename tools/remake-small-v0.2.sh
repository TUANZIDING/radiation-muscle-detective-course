#!/bin/bash
# usage: remake-small-v0.2.sh <ep> <ver>  re-encode the ≤38MB 720p copy from the 1080p master
EP=$1; V=$2; R=${RM_ROOT:-.}; cd $R
M=render/after-the-beam-ep$EP-$V.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $M); VB=$(python3 -c "print(int(37.5*8192/$DUR-60))")
ffmpeg -y -v error -i $M -vf "scale=1280:720" -c:v libx264 -preset slow -b:v ${VB}k -maxrate 450k -bufsize 900k -c:a aac -b:a 56k -movflags +faststart /tmp/ep$EP-small.mp4 && cp /tmp/ep$EP-small.mp4 render/after-the-beam-ep$EP-$V-small.mp4
ls -la render/after-the-beam-ep$EP-$V-small.mp4
