[Previous](..)
## 인코딩된 파일 bytes로 열어서 print로 출력하기
파일을 열때 'r'로 열면 그냥 str타입으로 열리지만 'rb'로 열면 bytes타입으로 로드된다.

    f=open('filename.sql','rb')
    for line in f:
    	a = line.decode('euc_kr', errors='ignore')
    	print(a)
    f.close()
