import cx_Oracle


def getMax():
    conn=cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    rs = cs.execute( "select nvl(max(pan)+1,1) as maxpan from omok")
    max_pan = 0
    for record in rs:
        max_pan = int(record[0])
    cs.close()
    conn.close()
    return max_pan

def writeHistroy(pan, history, win):
    conn=cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    
    sql = "insert into omok(pan, pseq, history, win) values (:1,:2,:3,:4)"
    
    for i,h in enumerate(history):
        cs.execute(sql,(pan, i, h, win))
    
    conn.commit()    
    cs.close()
    conn.close()
    
# max_pan = getMax()
# print(max_pan)
    

history = [1,2]
pan = 1
win = 2

writeHistroy(pan, history, win)









