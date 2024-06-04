> [Python Snippets](../README.md) / [각종 조각코드 모음](README.md) / ODBC, MS Acess.md
## ODBC, MS Acess
    import odbc
    
    def get_pg_ver(db_alias):
        connection = odbc.odbc(db_alias)
        try:
        	cursor = connection.cursor()
        	cursor.execute('SELECT version()')
        	for row in cursor.fetchall():
        		print row[0]
        finally:
        	connection.close()
    
    get_pg_ver('odbc_name/user/passwd')