[CONTENTS](README.md)
## pyopencl - OverflowError: int too big to convert
같은 문제에 대한 글이 있다. 참고하자.
https://lists.tiker.net/pipermail/pyopencl/2011-January/000489.html


아래와 같이 pyopencl로 초기화 부분인 cl.Context에서 OverflowError가 발생하는 경우가 있다.
해결책중에는 long 타입으로 바꾸어 보라는 의견이 있는데 나는 이것보다는 demo.py에서 context를 얻어오는 부분을 선택했다.

Traceback (most recent call last):
  File "gl_particle_animation.py", line 144, in <module>
    context = cl.Context(properties=[(cl.context_properties.PLATFORM, platform)] + get_gl_sharing_context_properties())
  File "E:\Anaconda\envs\condaPython\lib\site-packages\pyopencl\cffi_cl.py", line 665, in __init__
    dev_type))
OverflowError: int too big to convert

----------

platform = cl.get_platforms()[0]
context = cl.Context(properties=[(cl.context_properties.PLATFORM, platform)] + get_gl_sharing_context_properties())  

이부분에서 에러가 발생하는데 아래와 같이 바꿔주자

context = cl.create_some_context()