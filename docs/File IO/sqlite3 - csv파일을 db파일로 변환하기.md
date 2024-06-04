[Previous](..)
## sqlite3 - csv파일을 db파일로 변환하기
    import sqlite3
    import csv
    import os
    import glob
    import logging
    import codecs
    import sys
    import configparser
    
    # get logger
    logger = logging.getLogger('csv2db_logger')
    logger.setLevel(logging.DEBUG)
    
    # remove old log file
    logFileName = os.path.splitext(os.path.basename(__file__))[0] + ".log"
    if os.path.exists(logFileName):
        os.remove(logFileName)
    
    # set handler
    fileHandler = logging.FileHandler(logFileName)
    streamHandler = logging.StreamHandler()
    
    # set log fomatter
    fomatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')
    fileHandler.setFormatter(fomatter)
    streamHandler.setFormatter(fomatter)
    
    # attach log handler
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    
    # conver csv to database
    def csv2db():
        # initalize
        db = "db.sqlite3"
        conn = sqlite3.connect(db)
        conn.text_factory = str  # allows utf-8 data to be stored
        cur = conn.cursor()
    
        # traverse the directory and process each .csv file
        for csvfile in glob.glob(os.path.join("csv", "*.csv")):
            # remove the path and extension and use what's left as a table name
            tablename = os.path.splitext(os.path.basename(csvfile))[0]
    
            logger.info("Open %s file" % csvfile)
            
            for encoding in ['euc-kr', 'cp949', 'utf-8', 'utf-16-le', 'utf-16', 'utf-16-be']:
                with codecs.open(csvfile, "r",  encoding=encoding) as f:
                    reader = csv.reader(f)
                    # check file encoding
                    try:
                        reader = list(reader)
                    except:
                        continue
                        
                    if reader and len(reader) > 0:
                        header = reader[0]
                        # drop old table
                        sql = "DROP TABLE IF EXISTS %s" % tablename
                        cur.execute(sql)
                        
                        # add quote for near 'GROUP' syntax error
                        header = ["'" + i + "'" for i in header]
                        columnCount = len(header)
    
                        # create table sql command, if id field not in table then make it.
                        if not any(['id' == column.lower() for column in header]):
                            sql = "CREATE TABLE %s (%s)" % (tablename, 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' + ", ".join(
                                ["%s" % column for column in header]))
                        else:
                            sql = "CREATE TABLE %s (%s)" % (tablename, ", ".join(["%s" % column for column in header]))
                        cur.execute(sql)
    
                        # insert sql command
                        sql = "INSERT INTO %s (%s) VALUES (%s)" % (tablename, ", ".join(header), ", ".join(["?" for i in header]))                    
                        
                        # insert values - ignore header
                        for i, row in enumerate(reader[1:]):
                            if len(row) < columnCount:
                                logger.warning("-" * 50)
                                logger.warning("%s : not matched row item count. %d line" % (tablename, i+2))
                                logger.warning("%s" % header)
                                logger.warning("%s" % row)
                                continue
                            cur.execute(sql, row[:columnCount])
    
                        # commit
                        conn.commit()
                        break
                    else:
                        logger.warning("%s file error" % csvfile)
            # not found encoding
            else:
                logger.warning("encoding error")
        cur.close()
        conn.close()
        logger.info("end")
    
    # run
    if __name__ == '__main__':
        csv2db()