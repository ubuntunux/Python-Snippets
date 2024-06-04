[CONTENTS](README.md)
## ProgressBar ( 진행바 ) 출력하기
tqdm 라이브러리를 이용한 방법

```
from tqdm import tqdm
from time import sleep

for i in tqdm(range(int(100))):
    sleep(0.01)
```

source link : [https://stackoverflow.com/questions/4897359/output-to-the-same-line-overwriting-previous-output-python-2-5](https://stackoverflow.com/questions/4897359/output-to-the-same-line-overwriting-previous-output-python-2-5)

Example1) 직접 구현하기

```
def progressBar(value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()
```


Example2) 직접 구현하기

```
def startprogress(title):
    """Creates a progress bar 40 chars long on the console
    and moves cursor back to beginning with BS character"""
    global progress_x
    sys.stdout.write(title + ": [" + "-" * 40 + "]" + chr(8) * 41)
    sys.stdout.flush()
    progress_x = 0


def progress(x):
    """Sets progress bar to a certain percentage x.
    Progress is given as whole percentage, i.e. 50% done
    is given by x = 50"""
    global progress_x
    x = int(x * 40 // 100)                      
    sys.stdout.write("#" * x + "-" * (40 - x) + "]" + chr(8) * 41)
    sys.stdout.flush()
    progress_x = x


def endprogress():
    """End of progress bar;
    Write full bar, then move to next line"""
    sys.stdout.write("#" * 40 + "]\n")
    sys.stdout.flush()
```