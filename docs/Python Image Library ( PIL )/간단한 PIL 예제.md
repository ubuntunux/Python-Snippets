```
http://mataeoh.egloos.com/7063973

PIL은 Python의 가장 유명한 Image Processing 라이브러리이다.  python3에서는 pillow로 대체되었다.

# 파일 열기
import os
from PIL import Image
im = Image.open(filename)

# 빈 이미지 파일
empty_im = Image.new("RGB", (512, 512), "white")

# 이미지 크기
print im.size

#이미지 정보
print im.info

#이미지 포맷
print im.format

#이미지 모드
print im.mode

# rgba 포맷으로 변환
rgba_im = im.convert("RGBA")

# 픽셀값 알아내기
print im.getpixel( (x좌표, y좌표) )

# 픽셀값 입력하기 - RGBA 모드일때 : 0 ~255
im.putpixel( (x좌표, y좌표), ( R, G, B, A) )

# 빠른 Access를 위한 데이터 변환 - getpixel, putpixel보다 빠르다. 또한 im_raw의 값을 바꾸면 원래의 이미지도 바뀐다.
im_raw = im.load()
print im_raw[0,0]
im_raw[0,0] = (255, 255, 255, 255)
print im.getpixe((0,0)) # linked to im <--> im_raw

# png로 이미지 저장
new_filename = os.path.splitext(filename)[0] + '.png'
im.save(new_filename, format="png")
```