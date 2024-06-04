[Previous](..)
## sRGB
PIl은 sRGB 이미지를 불러오던 linear RGB를 불러오던 모두 선형으로 데이터를 변환한다.

sRGB 이미지를 open하면 pow(color, 2.2)를 해주어 선형으로 만들어 버리고

linear RGB 이미지는 그냥 그값을 그대로 사용한다.

그러므로 OpenGL에서 텍스쳐로 sRGB 이미지를 사용할때에는 주의 해야 한다.

??? 이거는 내가 제대로 테스트해본건지 확인이 필요하다...