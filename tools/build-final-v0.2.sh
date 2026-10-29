#!/bin/bash
# usage: build-final-v0.2.sh <ep> <ver>   (needs /tmp/ep<ep>-part0..3.mp4 and audio/ep<ep>-mix-v0.1.wav)
set -e
EP=$1; V=$2; R=${RM_ROOT:-.}; cd $R
if [ ! -f audio/ep$EP-mix-v0.1.wav ]; then
ffmpeg -y -v error -i audio/ep$EP-narration-v0.1.wav -i audio/ep$EP-piano-v0.1.wav -filter_complex \
 "[0:a]aformat=sample_rates=48000:channel_layouts=stereo,apad=pad_dur=12[v];[1:a]volume=0.05,highpass=f=90[p];[v][p]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[a]" \
 -map "[a]" -c:a pcm_s16le audio/ep$EP-mix-v0.1.wav
fi
rm -f /tmp/parts$EP.txt; for f in $(ls $R/render/parts/ep$EP-part*.mp4 | sort -V); do echo "file '$f'" >> /tmp/parts$EP.txt; done
ffmpeg -y -v error -f concat -safe 0 -i /tmp/parts$EP.txt -i audio/ep$EP-mix-v0.1.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 160k -shortest -movflags +faststart /tmp/ep$EP-full.mp4
cp /tmp/ep$EP-full.mp4 render/after-the-beam-ep$EP-$V.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/ep$EP-full.mp4); VB=$(python3 -c "print(int(37.5*8192/$DUR-60))")
ffmpeg -y -v error -i /tmp/ep$EP-full.mp4 -vf "scale=1280:720" -c:v libx264 -preset slow -b:v ${VB}k -maxrate 450k -bufsize 900k -c:a aac -b:a 56k -movflags +faststart /tmp/ep$EP-small.mp4
cp /tmp/ep$EP-small.mp4 render/after-the-beam-ep$EP-$V-small.mp4
ls -la render/after-the-beam-ep$EP-$V*.mp4; ffprobe -v error -show_entries format=duration -of csv=p=0 render/after-the-beam-ep$EP-$V.mp4
