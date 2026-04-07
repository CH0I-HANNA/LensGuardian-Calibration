import os
import numpy as np
import cv2

# 1. 체스보드 설정 (내부 교차점 개수)
CHECKERBOARD = (6, 4)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# 2. 3D 실제 세계 좌표 준비 (수정 완료)
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

objpoints = []  # 3D 점
imgpoints = []  # 2D 점

# 3. 영상 로드
base_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(base_dir, 'chessboard.mp4')
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("에러: 영상을 찾을 수 없습니다. 경로를 확인하세요!")
    exit()

print("분석 시작...")

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 체스보드 코너 찾기
    ret_cb, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret_cb:
        objpoints.append(objp)

        # 코너 정밀화
        corners2 = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1), criteria
        )
        imgpoints.append(corners2)

        # 디버깅용 시각화
        cv2.drawChessboardCorners(frame, CHECKERBOARD, corners2, ret_cb)

    cv2.imshow('Frame', frame)

    # ESC 누르면 종료
    if cv2.waitKey(50) & 0xFF == 27:
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

print(f"\n총 프레임 수: {frame_count}")
print(f"검출된 체스보드 수: {len(objpoints)}")

# 4. 캘리브레이션 수행
if len(objpoints) > 0:
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints,
        imgpoints,
        gray.shape[::-1],
        None,
        None
    )

    print("\n--- Calibration Results ---")
    print(f"RMS Error: {ret}")
    print(f"Camera Matrix (K):\n{mtx}")
    print(f"Distortion Coefficients:\n{dist}")

    # 저장
    output_path = os.path.join(base_dir, "calib_data.npz")
    np.savez(output_path, mtx=mtx, dist=dist)
    print(f"\n'{output_path}' 저장 완료!")

else:
    print("체스보드 검출 실패!")
    print("👉 CHECKERBOARD 값이 실제 체스보드와 맞는지 확인하세요.")