[Previous](..)
## Eclipse, PyCharm에서 LD_LIBRARY_PATH를 인식 못할때 ( profile과 .bashrc의 차이 ) 
http://mataeoh.egloos.com/7069644

나처럼 아주아주 황당한 경우를 겪은 사람에게 도움이 되었으면 좋겠다.
현재 사용중인 os는 ubuntu.
python으로 프로그래밍을 하던중 터미널창에서는 잘 실행되던것이 Eclipse, PyCharm으로 실행을 하면 라이브러리 파일(.so)을 찾지 못하겠다며 에러를 내뿜는 상황이 발생했다.
나는 환경변수 LD_LIBRARY_PATH가 뭔가 잘못됐음을 직감했다.
터미널에서 확인해 본 LD_LIBRARY_PATH값과 Eclipse, PyCharm에서 확인해본 LD_LIBRARY_PATH의 값이 서로 달랐던 것 이었다... 뜨아!!!

문제는 사실 아주 간단한 것 이었다. 결론부터 얘기하면 LD_LIBRARY_PATH 환경변수를 ~/.bashrc 파일에 설정해 두었기 때문에 생긴 문제였다.
그렇다면 어째서 같은 환경변수인데 터미널일 때와 아닐때 달랐던 것일까? (아.. 리눅스를 좀 아시는 분이라면 풉~~! 하고 웃었을 상황인듯 하다)
리눅스에는 login shell과 non-login shell, 즉 로그인쉘과 비로그인 쉘이 존재하는데 비로그인 쉘이란 os가 부팅되었을때 로그인 없이도 전체사용자에게 적용되는 쉘을 말한다. 비로그인 쉘이 실행되면서 /etc/profile과 /etc/bashrc 스크립트가 실행된다.
반대로 로그인쉘은 터미널창을 열때 로그인된 사용자에게만 실행되는 쉘이며 ~/.bashrc, ~/.profile, ~/.bash_profile등의 스크립트가 실행된다.

그렇다!! 처음으로 돌아가서 python 코드를 터미널창에서 실행했을때 잘되었던 이유는 LD_LIBRARY_PATH를 .bashrc에 설정해두었기 때문에 터미널창이 실행되며 해당 환경변수가 적용되었던 것이고 Eclipse, Pycharm을 실행할때에는 터미널창이 아닌 바탕화면에 깔린 바로가기 아이콘을 통해 실행하였기 때문에 bash쉘이 실행되지 않아 환경변수가 적용되지 않았던 것이다..
이문제는 리눅스 시스템에 대해 조금이라도 알았더라면 쉽게 풀수있는 문제인것이다.
앞으로는 bash shell을 사용하는 경우가 아니면 /etc/profile에 설정해두어야겠다..ㅠㅠ

좀더 자세한 내용은 아래의 글을 참조~

참고문서 : Login shell vs Non-login shell