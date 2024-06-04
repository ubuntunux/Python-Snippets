[Previous](..)
## sqlite3 - DB파일안의 테이블 리스트 출력하기
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())