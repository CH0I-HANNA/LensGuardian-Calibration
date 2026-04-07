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
분석 영상(`chessboard.mp4`)을 통해 산출된 카메라의 고유 파라미터 값입니다.

### 📍 요약 정보
* **총 분석 프레임**: 61개
* **검출된 체스보드 수**: 61개 (검출 성공률 100%)
* **평균 재투영 오차 (RMS Error)**: **`0.153198`**
  * *분석: 0.15 수준의 RMSE는 매우 정밀한 캘리브레이션 결과로, 산출된 파라미터의 신뢰도가 매우 높음을 의미합니다.*

### 📍 내부 파라미터 (Intrinsic Parameters)
카메라 행렬($K$)을 통해 산출된 초점 거리와 주점 좌표입니다.

| 항목 | 의미 | 산출 값 (Pixel) |
| :--- | :--- | :--- |
| **fx** | 가로 방향 초점 거리 | **1883.44** |
| **fy** | 세로 방향 초점 거리 | **1874.67** |
| **cx** | 렌즈 중심 X 좌표 (Principal Point X) | **656.67** |
| **cy** | 렌즈 중심 Y 좌표 (Principal Point Y) | **366.08** |

### 📍 왜곡 계수 (Distortion Coefficients)
렌즈의 굴곡에 의한 왜곡 정도를 나타내는 계수입니다.
* **값**: `[[-2.2615, 3.8133, -0.0081, -0.0164, -117.1787]]`
* **분석**: $k_3$ 값이 매우 크게 산출된 것으로 보아, 주변부 왜곡이 강한 광각 렌즈가 사용되었음을 알 수 있으며 프로그램이 이를 강력하게 보정하고 있습니다.

## 💻 camera_calibration.py 코드 실행 결과 (터미널 & 분석하고 있는 순간의 스크린 샷)
### 터미널
<img width="845" height="328" alt="Image" src="https://github.com/user-attachments/assets/f3f67334-bb26-49ff-b18d-745a6d652f96" />

### 스크린 샷
<img width="1392" height="860" alt="Image" src="https://github.com/user-attachments/assets/1729eeed-b35d-4a36-bd31-7a21e725c03d" />

## 🖼️ Lens Distortion Correction 결과
산출된 $K$ 행렬과 왜곡 계수를 적용하여 영상을 평탄화한 결과입니다.

| 원본 영상 (Original) | 왜곡 보정 후 (Undistorted) |
| :---: | :---: |
| ![Image](https://github.com/user-attachments/assets/423050f8-a1ef-468c-b8d9-ee42a60c6849) | ![Image](https://github.com/user-attachments/assets/505a3854-434d-4ce2-96a6-16ee09c66f6e) |
> **결과 해석**: 왼쪽(원본)에서 바깥쪽으로 볼록하게 휘어 보이던 체스보드의 격자선들이 보정 후(오른쪽)에는 수학적으로 계산된 직선으로 바르게 복원되었습니다.

