> [Python Snippets](../README.md) / [Logging](README.md) / logging 모듈 밀리세컨드 단위까지 표시하기.md
## logging 모듈 밀리세컨드 단위까지 표시하기
```
logging.Formatter('[%(levelname)-8s|%(filename)s:%(lineno)s] %(asctime)s.%(msecs)03d > %(message)s',"%Y-%m-%d %H:%M:%S")
```