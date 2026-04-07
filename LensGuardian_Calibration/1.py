import os
import cv2  # ✅ 이거 추가
import numpy as np

base_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(base_dir, 'chessboard.mp4')

print(video_path)
print(os.path.exists(video_path))

cap = cv2.VideoCapture(video_path)