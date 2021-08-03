import cx_Oracle

conn=cx_Oracle.connect("python/python@localhost:1521/xe")

cs = conn.cursor()
# 자바에서 statement와 같다
cs.execute( "select col01, col02, col03 from sample")
for record in cs :
    print(record)
cs.close()
conn.close()
