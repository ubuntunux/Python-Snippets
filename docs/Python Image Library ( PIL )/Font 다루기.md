> [Python Snippets](../README.md) / [Python Image Library ( PIL )](README.md) / Font 다루기.md
## Font 다루기
유니코드를 입력해서 text.jpg파일로 저장하는 예제이다. 아래 코드를 실행한후 이미지 뷰어로 text.jpg 파일을 열어보면 텍스트가 그려져 있을것이다.

```
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#configuration
font_size=36
width=500
height=100
back_ground_color=(255,255,255)
font_size=36
font_color=(0,0,0)
unicode_text = u"\u2605" + u"\u2606" + u"Текст на русском" + u"파이썬"

im  =  Image.new ( "RGB", (width,height), back_ground_color )
draw  =  ImageDraw.Draw ( im )
unicode_font = ImageFont.truetype("ARIALUNI.TTF", font_size)
draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )

im.save("text.jpg")
```