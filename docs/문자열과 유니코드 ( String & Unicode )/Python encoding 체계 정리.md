> [Python Snippets](../README.md) / [문자열과 유니코드 ( String & Unicode )](README.md) / Python encoding 체계 정리.md
## Python encoding 체계 정리
```
Python encoding 체계 정리


Python을 접하다보면 아래와 같은 encoding 문제를 자주 마주하게 된다.

 UnicodeDecodeError : 'utf8' codec can't decode byte 0xb9 in position 0: invalid start byte. You passed in '\xb9\xcc\xb5\xee\xb7\xcf+\xbc\xad\xba\xea\xb0\xa1\xb8\xcd\xc1\xa1+\xc0\xd4\xb4\xcf\xb4\xd9.' (<type 'str'>)


보통 이런 경우 Default Encoding Type과 파일로 부터 읽어들인 Encoding이 다르기 

때문에 decode할 수 없어 에러가 발생한다.

내 시스템의 Default Encoding이 utf-8이고 외부 서버로부터 전송받은, 혹은 파일의 

Encoding이 euc-kr이라면 아래와 같이 utf-8으로 변환 해줘야 한다.

 
  euc_bytes = '\xc0\xfc\xb9\xae \xc6\xc4\xbd\xcc \xc1\xdf \xbf\xc0\xb7\xf9\xb0\xa1 \xb9\xdf\xbb\xfd\xc7\xdf\xbd\xc0\xb4\xcf\xb4\xd9.'
  utf_bytes = unicode(euc_bytes,'euc-kr').encode('utf-8')
  print euc_bytes
  print utf_bytes

실제로 결제 PG연동 시, 우리 내부 시스템은 utf-8환경이였고, 외부 PG사의 경우 euc-kr을 

지원하고 있었기 때문에 모든 응답 메세지를 euc-kr로 받을 수 밖에 없었고, 한글 응답 

메세지는 모두 utf-8으로 encoding하여 사용하였다.



이런 현상을 이해하기 위해 unicode에 대한 이해를 할 필요가 있다.

unicode는 전세계의 모든 문자를 처리 가능하도록 설계된 방식이다.

utf-8도 unicode에 기반한 인코딩 방식이다.

euc-kr의 경우 한글 2byte의 완성형 인코딩 셋이고(가 = AC+00)  utf-8은 조합형 

(가 = 'ㄱ + ㅏ', EA + B0 + 80) 초중종성 세 바이트를 조합하는 조합형 인코딩 셋이다.

따라서 euc-kr로 인코딩된 바이트를 unicode로 변경 후(2byte), 변경된 unicode를 다시 

utf-8으로 변경하는 작업을 해야 된다.

예를 들어 보면.

euc_to_utf8.py

 
  #-*- coding: utf-8 -*-
  test_utf8 = 'rocksea 블로그'
  test_euckr = unicode(test_utf8,'utf-8').encode('euc-kr')
  print test_utf8
  print test_euckr
  print unicode(test_euckr,'euc-kr').encode('unicode-escape')
  print unicode(test_euckr,'euc-kr')

result

$ python euc_to_utf.py

rocksea 블로그

rocksea ▒▒α▒

rocksea \ube14\ub85c\uadf8

rocksea 블로그



현재 시스템이 utf-8이기 때문에 euc-kr의 경우 인코딩이 깨져서 보인다.

하지만 unicode로 인코딩 후 escape문자열을 살펴보면 아래와 같다.

rocksea \ube14\ub85c\uadf8

'rocksea'의 경우 영문 ascii코드(1byte)이기 때문에 그대로 출력이 되지만

'블로그'의 경우엔 unicode로 변환하여 출력한다. 





[그림 1] '블(\uBE14)'에대한 유니코드표





[그림 2] '로(\uB85C)'에대한 유니코드표





[그림 3] '그(\uADF8)'에대한 유니코드표


이렇듯 utf-8시스템에서의 euc-kr 바이트를 unicode로 encoding을 해야 

UnicodeDecodeError : 'utf8' codec can't decode byte 

에러를 피할 수 있을 것이다.

```

참고 사이트 : 

http://munjanet.net/display/home.php?mode=kosoboard_view&szTblName=fontmunja&page=3&id=197&szFid=-197&szDepth=1&limit=&keykind=&keyword=

http://sexy.pe.kr/tc/113



출처: http://rocksea.tistory.com/332 [Rocksea - knowledge creator]