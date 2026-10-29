#!/bin/bash
# usage: run-render-v0.2.sh <ep> <data> <part> <nparts>  -> render/parts/ep<ep>-part<part>.mp4 (copied from /tmp; /tmp is not durable)
cd ${RM_ROOT:-.}
python3 -c "import cv2" 2>/dev/null || pip install -q opencv-python-headless edge-tts >/dev/null 2>&1
python3 script/render-video-v0.2.py "$@" && cp /tmp/ep$1-part$3.mp4 render/parts/ && rm -f /tmp/ep$1-part$3.mp4
