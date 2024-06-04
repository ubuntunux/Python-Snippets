[Previous](..)
## command 'gcc' failed with exit status 1
    distutils.errors.DistutilsError: Setup script exited with error: command 'gcc' failed with exit status 1


Debian이나 Ubuntu에서 위와 같은 에러발생시 아래의 명령을 실행하여 의존 패키지를 설치하면 에러가 해결된다.


    sudo apt-get install build-essential libssl-dev libffi-dev python-dev