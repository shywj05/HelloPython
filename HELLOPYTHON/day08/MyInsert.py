import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")
cs = conn.cursor()
sql = "insert into SAMPLE(col01, col02, col03) values (:1,:2,:3)"
cs.execute(sql,('5','5','5'))
print(cs.rowcount)

conn.commit()    
cs.close()
conn.close()

