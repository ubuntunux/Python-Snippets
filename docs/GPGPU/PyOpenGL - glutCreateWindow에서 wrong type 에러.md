[CONTENTS](README.md)
## PyOpenGL - glutCreateWindow에서 wrong type 에러
pyopengl을 테스트 해보려고 실행했느데 glutCreateWindow("hello opengl")와 같이 초기화 함수에서 에러가 발생했다.

    Traceback (most recent call last):
      File "gl_particle_animation.py", line 133, in <module>
        window = glut_window()
      File "gl_particle_animation.py", line 29, in glut_window
        window = glutCreateWindow("Particle Simulation")
      File "E:\Anaconda\envs\condaPython\lib\site-packages\OpenGL\GLUT\special.py", line 73, in glutCreateWindow
        return __glutCreateWindowWithExit(title, _exitfunc)
    ctypes.ArgumentError: argument 1: <class 'TypeError'>: wrong type

구글을 찾아보니 glutCreateWindow 함수 호출시 인자로 string을 넘겨주는데 이때 바이트 스트링 타입으로 넘겨주어야 한다.
즉 glutCreateWindow(b"hello opengl")과 같이 스트링 앞에 b를 붙여주어야 한다.