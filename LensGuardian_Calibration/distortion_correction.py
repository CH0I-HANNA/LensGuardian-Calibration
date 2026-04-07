import numpy as np
import cv2
import os

# 1. 파일 경로 설정
base_dir = os.path.dirname(os.path.abspath(__file__))
calib_path = os.path.join(base_dir, 'calib_data.npz')

# 데이터 로드 확인
if not os.path.exists(calib_path):
    print(f"에러: '{calib_path}' 파일을 찾을 수 없습니다. 캘리브레이션을 먼저 실행하세요.")
    exit()

data = np.load(calib_path)
mtx = data['mtx']
dist = data['dist']

# 영상 경로 설정 (data 폴더 안의 chessboard.avi 사용)
video_path = os.path.join(base_dir, 'chessboard.mp4')
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"에러: 영상을 열 수 없습니다. 경로를 확인하세요: {video_path}")
    exit()

print("왜곡 보정 데모 시작...")

# 첫 번째 프레임을 읽어서 크기와 FPS 얻기
ret, frame = cap.read()
if not ret:
    print("영상을 읽을 수 없습니다.")
    cap.release()
    exit()

h, w = frame.shape[:2]
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 30  # 기본 FPS

# 2. 자유 조정 파라미터 (alpha) 적용
# alpha=0: 왜곡을 제거하면서 남는 검은 여백을 잘라냄
# alpha=1: 모든 픽셀을 유지 (약간의 검은 여백이 생길 수 있음)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# 출력 동영상 설정
output_path = os.path.join(base_dir, 'undistorted_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

# 첫 번째 프레임 처리
dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)
out.write(dst)

# 나머지 프레임 처리
while True:
    ret, frame = cap.read()
    if not ret:
        break
    dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)
    out.write(dst)

cap.release()
out.release()
print(f"왜곡 보정된 동영상을 저장했습니다: {output_path}")