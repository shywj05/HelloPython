import cx_Oracle
import datetime


conn=cx_Oracle.connect("python/python@localhost:1521/xe")
cs = conn.cursor()
sql = "insert into SAMPLE(col01, col02, col03) values (:1,:2,:3)"
now1 = datetime.datetime.now()
for i in range(10000):
    cs.execute(sql,('5','5','5'))
now2 = datetime.datetime.now()
 
conn.commit()    
cs.close()
conn.close()

ellapse = now2-now1
print("ellapse",ellapse)
