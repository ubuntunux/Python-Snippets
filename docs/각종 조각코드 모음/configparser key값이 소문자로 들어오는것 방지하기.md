[CONTENTS](README.md)
## configparser key값이 소문자로 들어오는것 방지하기
ConfigParser를 사용하다보면 이상한점이 한가지 있다. 아래와 같이 SHADER_DEFINE_TEST라는 값이 있는데 python으로 해당값을 실제 가져와보면 소문자로 바뀌어 있는것이다.
    
    [Define]
    SHADER_DEFINE_TEST = 1
    
ConfigParser의 클래스를 살펴보면 아래와 같은 함수가 있는데 보는것처럼 lower()로 변환해주고 있다. 이것을 방지하려면 해당 함수를 override해서 소문자로 바뀌지 않게 해주자.
    
    def optionxform(self, optionstr):
        return optionstr.lower()
               
이렇게 바꾸어 보자.

config_test = configparser.ConfigParser()
config_test.optionxform = lambda optionstr: optionstr

보는것처럼 람다로 들어온값을 리턴하도록 되어있다. 