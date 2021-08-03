import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")

cs = conn.cursor()
# 자바에서 statement와 같다
rs = cs.execute( "select nvl(max(pan)+1,1) as maxpan from omok")

max_pan = 0
for record in rs:
    max_pan = int(record[0])
    
print(max_pan)

cs.close()
conn.close()
