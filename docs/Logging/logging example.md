> [Python Snippets](../README.md) / [Logging](README.md) / logging example.md
## logging example
logging 예제)

```
import logging

format='%(asctime)s,%(msecs)03d [%(levelname)s|%(filename)s:%(lineno)d] %(message)s'
datefmt='%Y-%m-%d:%H:%M:%S'
logging.basicConfig(format=format, datefmt=datefmt, level=logging.DEBUG)

logging.debug("debugging test")
logging.info("infomation test")
logging.warning("warnning test")
logging.error("error test")
logging.critical("critical test")
```


Log를 파일로 저장하기

```
import datetime
import logging
from logging.handlers import RotatingFileHandler
import os
import time


def create_logger(logger_name, log_dirname, level):
    # prepare log directory
    if not os.path.exists(log_dirname):
        os.makedirs(log_dirname)
    log_file_basename = datetime.datetime.fromtimestamp(time.time()).strftime(f'{logger_name}_%Y%m%d_%H%M%S.log')
    log_filename = os.path.join(log_dirname, log_file_basename)

    # create logger
    logger = logging.getLogger(log_dirname)
    logger.setLevel(level=level)

    # add handler
    stream_handler = logging.StreamHandler()
    file_max_byte = 1024 * 1024 * 100 #100MB
    backup_count = 10
    file_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=file_max_byte, backupCount=backup_count)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    # set formatter
    formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)03d [%(levelname)s|%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    return logger

logger = create_logger(logger_name='test', log_dirname='.log', level=logging.DEBUG)
logger.info("Test")
```