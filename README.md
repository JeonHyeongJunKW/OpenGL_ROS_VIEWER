# OpenGL_ROS_VIEWER
python2.7 환경에서 ROS 토픽으로 얻은 이미지 위에 Pyopengl을 통해서,
사각형 박스를 만드는 코드입니다.
## 코드 설명
### viwer.py
viewer.py 코드는 ROS를 기반으로 이미지 토픽을 받는 부분과 Pyopengl에 대한 멀티프로세스와 공유변수를 만드는 부분으로 구성되어있습니다. 

### OpenGL_runner.py
OpenGL_runner.py의 경우 pyopengl코드를 pygame라이브러리를 기반으로 돌리고 있습니다.

### Itembox.py
화면상에 Pyopengl로 박스를 만들 때, 박스의 생성과 위치, 회전등을 결정할 수 있습니다. 

## 구현환경
- Ubuntu 18.04LTS
- Python 2.7.17
- pygame 2.0.1
- opencv-python 4.2.0.32
- PyOpenGL 3.1.5
- PyOpenGL-accelerate 3.1.5

