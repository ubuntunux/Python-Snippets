```
sdl2 - ImportError: DLL load failed: 지정된 모듈을 찾을 수 없습니다.
  File "D:\Anaconda3\envs\ModernGL\lib\site-packages\kivy\core\__init__.py", line 59, in core_select_lib
    fromlist=[modulename], level=0)
  File "D:\Anaconda3\envs\ModernGL\lib\site-packages\kivy\core\text\text_sdl2.py", line 12, in <module>
    from kivy.core.text._text_sdl2 import (_SurfaceContainer, _get_extents,

pil - ModuleNotFoundError: No module named 'PIL'
  File "D:\Anaconda3\envs\ModernGL\lib\site-packages\kivy\core\__init__.py", line 59, in core_select_lib
    fromlist=[modulename], level=0)
  File "D:\Anaconda3\envs\ModernGL\lib\site-packages\kivy\core\text\text_pil.py", line 7, in <module>
    from PIL import Image, ImageFont, ImageDraw

[CRITICAL] [App         ] Unable to get a Text provider, abort.
```

```
pip install kivy.deps.sdl2
pip install kivy.deps.glew
```
