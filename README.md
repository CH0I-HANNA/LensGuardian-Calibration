# LensGuardian-Calibration 🛡️

OpenCV를 활용하여 카메라의 고유 파라미터를 추출하고, 렌즈로 인해 발생하는 왜곡(Distortion)을 보정하는 컴퓨터 비전 프로젝트입니다. 

## 📝 프로젝트 소개
일반적인 카메라는 렌즈의 기하학적 특성으로 인해 직선이 곡선으로 휘어 보이는 **배럴 왜곡(Barrel Distortion)** 현상이 발생합니다. 본 프로그램은 체스보드 패턴을 인식하여 카메라의 광학적 특성을 수학적으로 모델링(Calibration)하고, 이를 바탕으로 왜곡 없는 깨끗한 영상을 복원하는 기능을 제공합니다.

## 💡 핵심 기능
* 체스보드 내부 교차점(Internal Corners) 자동 검출 및 정밀화
* 카메라 내부 파라미터(Intrinsic Parameters) 및 왜곡 계수 산출
* 산출된 데이터를 활용한 실시간 영상 왜곡 보정 (Undistortion)

## 📷 사용한 체크보드 이미지
<img width="833" height="592" alt="Image" src="https://github.com/user-attachments/assets/d1f97469-8bb5-45ed-8c2d-547fd7f0ed9b" />

## 📁 파일 구조 및 실행 방법
camera_calibration.py: chessboard.mp4를 분석하여 calib_data.npz 생성

distortion_correction.py: 저장된 데이터를 불러와 왜곡 보정 수행 후 undistorted_video.mp4로 저장

calib_data.npz: 산출된 카메라 파라미터 저장 파일

## 📊 Camera Calibration 결과
영상 파일(`chessboard.mp4`)을 분석하여 도출된 데이터입니다.

* **총 분석 프레임**: 61개
* **검출된 체스보드 수**: 61개 
* **평균 재투영 오차 (RMS Error)**: `0.15319846774536547`

### 카메라 행렬 (Camera Matrix - K)
이미지 센서의 초점 거리와 중심점 좌표를 나타냅니다.
```text
[[1.88344039e+03 0.00000000e+00 6.56667814e+02]
 [0.00000000e+00 1.87467440e+03 3.66079226e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
```

### 왜곡 계수 (Distortion Coefficients)
렌즈의 휘어짐 정도를 나타내는 5개의 계수($k_1, k_2, p_1, p_2, k_3)입니다.
```text
[[-2.26151808e+00  3.81337308e+00 -8.15662339e-03 -1.64764347e-02 -1.17178707e+02]]
```

## 💻 camera_calibration.py 코드 실행 결과 (터미널 & 분석하고 있는 순간의 스크린 샷)
### 터미널
<img width="845" height="328" alt="Image" src="https://github.com/user-attachments/assets/f3f67334-bb26-49ff-b18d-745a6d652f96" />

### 스크린 샷
<img width="1392" height="860" alt="Image" src="https://github.com/user-attachments/assets/1729eeed-b35d-4a36-bd31-7a21e725c03d" />

## 🖼️ Lens Distortion Correction 결과
보정 데이터를 적용하여 직선이 휘어 보이던 현상을 해결한 결과입니다.

### 보정 전
![Image](https://github.com/user-attachments/assets/423050f8-a1ef-468c-b8d9-ee42a60c6849)

### 보정 후
![Image](https://github.com/user-attachments/assets/505a3854-434d-4ce2-96a6-16ee09c66f6e)

