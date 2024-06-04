> [Python Snippets](../../../README.md) / [각종 조각코드 모음](../../README.md) / [변수가 있는지 확인하기 ( hasattr ](../README.md) / [ getattr ](README.md) /  setattr ).md
##  setattr )
```
class cls:
    a = 1
    def b(self):
        pass

# cls에 b라는 멤버가 있는지 확인
>>> hasattr(cls, 'b')
True

# cls에서 a변수의 값 가져오기
>>> getattr(cls, 'a')
1

# cls의 a라는 변수에 값 9 설정하기
>>> setattr(cls, 'a', 9)
```