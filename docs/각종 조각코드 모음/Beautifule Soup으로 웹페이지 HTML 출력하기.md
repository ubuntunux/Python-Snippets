[CONTENTS](README.md)
## Beautifule Soup으로 웹페이지 HTML 출력하기
```
import requests
import urllib3
from bs4 import BeautifulSoup

# InsecureRequestWarning warning 메시지가 출력되지 않게 해준다.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# verify옵션은 SSLError를 방지해 준다.
r = requests.get("https://ta-airframe.ncsoft.com/app/my/dashboards", verify = False)

soup = BeautifulSoup(r.content)
print(soup.title)
```