[CONTENTS](README.md)
## PyOpenGL - AttributeError - 'numpy.ndarray' object has no attribute 'buffers' 
[Previous]()
## PyOpenGL - AttributeError: 'numpy.ndarray' object has no attribute 'buffers' 
동일한 문제에 관한 글이 있다. 참고하자
https://sourceforge.net/p/pyopengl/mailman/message/32863450/

pyopencl 예제를 실행하다 보면 아래와 같이 vbo(vertex buffer object)의 buffers를 참조하려다 에러가 나는 경우가 있다.

Traceback (most recent call last):
  File "D:\Development\PythonProject\PythonExamples\PyOpenCL\nbody_simulation\main.py", line 135, in <module>
    p2 = window()
  File "D:\Development\PythonProject\PythonExamples\PyOpenCL\nbody_simulation\main.py", line 59, in __init__
    self.cle.loadData(pos_vbo, col_vbo, vel)
  File "D:\Development\PythonProject\PythonExamples\PyOpenCL\nbody_simulation\part2.py", line 37, in loadData
    self.pos_cl = cl.GLBuffer(self.ctx, mf.READ_WRITE, int(self.pos_vbo.buffers[0]))
  File "vbo.pyx", line 177, in OpenGL_accelerate.vbo.VBO.__getattr__ (src\vbo.c:2754)
AttributeError: 'numpy.ndarray' object has no attribute 'buffers'

원인은 vbo 객체를 생성시 기본적으로는 PyOpenGL 라이브러리를 참조하나 PyOpenGL-accelerate가 설치되어 있을경우 PyOpenGL-accelerate로부터 vbo를 생성하는데, 3.0.2버전까지는 vbo객체에 buffers 멤버가 있었으나 3.1.0 버전부터 사라져 버려 AttributeError이 발생한다. ( pyopengl accelerate가 cython구현인데 고치기 힘든 버그가 있어서 buffers 부분을 빼버렸다고 한다. )

**buffers[0] 부분을 buffer로 바꾸어주면 해결된다.**

그래도 안된다면..
일단 임시로 pyopengl accelerate를 지우거나 아래와 같이 옵션을 꺼주도록 하자..ㅠㅠ
당연히 이 부분은 최상단에 추가해주어야 한다.

from OpenGL import _configflags
_configflags.USE_ACCELERATE = False