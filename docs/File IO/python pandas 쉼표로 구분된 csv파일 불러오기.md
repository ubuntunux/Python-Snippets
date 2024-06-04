[Previous](..)
## python pandas 쉼표로 구분된 csv파일 불러오기
쉼표로 구분된 csv파일을 그냥 불러올경우 파싱에러가 발생한다.
아래와 같이 quotechar 파라미터에 구분자를 넣어주면 해결된다.

    import pandas as pd
    doc = pd.read_csv("Deploy_Npc.csv", quotechar='.')