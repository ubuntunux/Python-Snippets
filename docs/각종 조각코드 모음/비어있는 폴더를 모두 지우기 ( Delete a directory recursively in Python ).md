> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / 비어있는 폴더를 모두 지우기 ( Delete a directory recursively in Python ).md
## 비어있는 폴더를 모두 지우기 ( Delete a directory recursively in Python )
```
import os

failed_list = []
def walk(path):
    contents = [os.path.join(path, x) for x in os.listdir(path)]
    dirnames = [x for x in contents if os.path.isdir(x)]
    filenames = [x for x in contents if os.path.isfile(x)]
    for dirname in dirnames:
        walk(dirname)

    if not dirnames and not filenames:
        try:
            os.removedirs(path)
        except:
            failed_list.append(path)  
        
    
walk('e:\\SomeDirectory')

print("Done")

```