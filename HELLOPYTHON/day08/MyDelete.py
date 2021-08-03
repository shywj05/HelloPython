import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")

cs = conn.cursor()
sql = "delete from sample where col01='99'"
cs.execute(sql)
print(cs.rowcount)

conn.commit()    
cs.close()
conn.close()