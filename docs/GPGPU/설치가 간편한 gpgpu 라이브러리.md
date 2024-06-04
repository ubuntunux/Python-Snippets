> [Python Snippets](../README.md) / [GPGPU](README.md) / 설치가 간편한 gpgpu 라이브러리.md
## 설치가 간편한 gpgpu 라이브러리
Python에서 gpu 프로그래밍을 위한 모듈중 가장 유명한 것은 아마도 pyopencl, pycuda일것 같다.
튜토리얼도 많고 opengl과의 연동, 확장가능하다는 측면에서 가장 공식적인 패키지이지만 설치가 까다로운것이 단점이다.
(예제들도 패키지 의존성이 많아 안되는것들도 있다.)

이리저리 검색을 하다보니 아래와 같이 cuda, opencl관련 python 모듈을 찾게되었다.

cuda4py : https://github.com/Samsung/cuda4py
opencl4py : https://github.com/ajkxyz/opencl4py

github주소를 보면 알겠지만 samsung관련 직원분이 만드신듯~ㅎ

어찌되었든 pycuda, pyopencl처럼 c코드를 컴파일하거나 하지 않는다. cffi를 이용해 작성되었기 때문이다.

간단하게 gpgpu 관련 테스트용도로 적합한듯하다. 또한 pypy에서도 잘돌아간단다~