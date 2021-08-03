import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")
cs = conn.cursor()

sql = "insert into omok(pan, pseq, history, win) values (:1,:2,:3,:4)"
cs.execute(sql,('1','1','1','1'))
print(cs.rowcount)

conn.commit()    
cs.close()
conn.close()

