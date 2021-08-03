import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")
cs = conn.cursor()
sql = "update sample SET col02=:1, col03=:2 where col01=:3"
cs.execute(sql,('4','4','5'))
print(cs.rowcount)

conn.commit()    
cs.close()
conn.close()