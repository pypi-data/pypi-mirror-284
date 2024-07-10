# YOLOv8_for_ROS2
ROS2 강의에서 YOLOv8 사물인식 파트에 대한 강의 자료


# Ubuntu 20.04, 22.04 초기 설정 및 YOLOv7 환경 구축

## 처음 우분투 세팅

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3.8-venv
```

## 가상환경 만들고 실행하기

```bash
python3.8 -m venv yolo
source yolo/bin/activate
```

## ROS2를 위한 YOLOv7 패키지 설치하기

```bash
pip install YOLOv7_with_depthmap
```

## 패키지가 제대로 설치되었는지 확인하기
```bash
source yolo/bin/activate
python
```
여기서 아래 처럼 출력되면 문제 없음(컴퓨터 환경에 따라 GPU를 사용할 수 없는 환경일 수도 있음)
```bash
>>> from YOLOv7_with_depthmap import YOLOv7
>>> model = YOLOv7()
GPU 사용 가능
```


## 강의 자료 코드 로컬에 불러오기

1. 우분투 터미널 실행

    ```bash
    mkdir YOLOv8_ROS2
    cd YOLOv8_ROS2
    git clone https://github.com/Nyan-SouthKorea/YOLOv8_for_ROS2.git
    ```
    clone된 해당 폴더로 이동

2. VS코드 실행(방금 위에서 생성한 yolo 가상환경 연결하기)

3. Ctrl + Shift + p 버튼을 누르고 "interpreter" 라고 검색하면 아래의 버튼으로 유도됨
![alt text](https://github.com/Nyan-SouthKorea/YOLOv7_with_depthmap/blob/main/README_images/image_1.png)


4. Enter interpreter path 선택
![alt text](https://github.com/Nyan-SouthKorea/YOLOv7_with_depthmap/blob/main/README_images/image_2.png)

5. Find -> .. -> yolo -> bin -> python3 선택

6. VS코드 종료 후 재 실행

7. 아무 코드나 실행해보자. 이 때 select interpreter에서 yolo가 보이면 선택

8. 이후 VS코드 관련 extension을 설치하라는 안내가 나오면 모두 설치해준다. 그리고 실행이 안되면 VS코드 재실행 반복

9. 우리가 만든 yolo라는 가상환경으로 코드를 돌릴 수 있도록 설정 마침

## 테스트 코드(실시간 webcam 인퍼런스)
```python
import cv2

model = YOLOv7()
cap = cv2.VideoCapture(0)
while True:
    # 이미지 읽기
    ret, img = cap.read()
    if ret == False:
        print('웹캠 수신 실패. 프로그램 종료')
        break

    # 추론
    result = model.detect(bgr_img=img)
    print(result)
    cv2.imshow('YOLOv7 test', model.draw())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
```

## 테스트 코드(폴더 안에 있는 이미지들 인퍼런스) (더미 depth map도 생성해 봅니다)
```python
import cv2
import os

model = YOLOv7()
path = 'test_img'
for img_name in os.listdir(path):
    # 이미지 읽기
    img = cv2.imread(f'{paht}/{img_name}')
    
    # dummy img 생성
    h, w, c = img.shape
    depth_map = np.random.randint(0, 256, (w, h), dtype=np.uint8)

    # 추론
    result = model.detect(bgr_img=img, depth_map=depth_map)
    print(result)
    cv2.imshow('YOLOv7 test', model.draw())

    # 클릭하면 다음 사진으로 넘어감
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
```

## 시연 비디오
아래 영상과 같이 저사항 노트북 환경에서 YOLOv8 추론 속도는 느리더라도, 비디오 스트리밍은 부드러운 것을 확인 가능합니다.
![alt text](https://github.com/Nyan-SouthKorea/YOLOv7_with_depthmap/blob/main/README_images/demo_video_1.gif)


## 라이센스
YOLOv7 라이센스를 따릅니다. 
https://github.com/WongKinYiu


## 관련 링크
github : https://github.com/Nyan-SouthKorea/YOLOv7_with_depthmap

pypi : 

Naver Blog : https://blog.naver.com/112fkdldjs 