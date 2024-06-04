[Previous](..)
## Notepad++에서 파이썬 활용하기
우선 쓸만한 플러그인부터 설치해보자



- Explorer : 왼쪽에 탐색기 창이 열림 ( 단축키 : Ctrl + Alt + Shift + e )
- NppExec : 콘솔 명령을 매크로로 입력할수 있는 플러그인
- Python Script
- PyNpp
- Compare
- Source Cookifier
- SourceSwitch


Python Script파일 실행 명령

NppExec를 설치하고 F6키를 누른 후 아래와 같이 입력

    cd "$(CURRENT_DIRECTORY)"
    cmd /K python "$(FULL_CURRENT_PATH)"