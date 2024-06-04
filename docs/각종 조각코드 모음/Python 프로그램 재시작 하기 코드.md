> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / Python 프로그램 재시작 하기 코드.md
## Python 프로그램 재시작 하기 코드
http://ahmedsoliman.com/2011/09/21/auto-restarting-python-application/

파이썬이 종료될때 자동으로 다시 재시작하는 예제이다.

```
import os, sys, time

def main():  
    print("AutoRes is starting")
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(1)
    print("Respawning")
    os.execvp(executable, args)

if __name__ == "__main__":  
    main()
```