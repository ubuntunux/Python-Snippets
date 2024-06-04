    import pymssql
    conn = pymssql.connect(host='10.3.201.80', user='SMILEGATE\\thyoon', password='password', database='DataViewer')
    cur = conn.cursor()
    cur.execute("SELECT TOP 1000 [ID] ,[Mesh] ,[Material1] ,[Material2] ,[Material3] ,[Material4] ,[AnimSet1] ,[AnimSet2] ,[AnimSet3] ,[AnimSet4] ,[LookInfoKey] ,[Description] ,[SubmittedBy] ,[PhysicsAsset] ,[ActionGroup] ,[AnimTree] ,[ImageSource] ,[ModelingSource] ,[VariationType] ,[Tag]  FROM [DataViewer].[dbo].[ResourceData]")
    row = cur.fetchone()
    while row:
        print "ID=%d, Mesh=%s" % (row[0], row[1])
        row = cur.fetchone()
    conn.close()