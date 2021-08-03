import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import cx_Oracle
import numpy as np

conn=cx_Oracle.connect("python/python@localhost:1521/xe")
cs = conn.cursor()
    
def getPrice(S_NAME):
    rs = cs.execute("SELECT S_PRICE FROM STOCK WHERE S_NAME = '"+S_NAME+"' ORDER BY S_INTIME")
    ret = []
    for record in rs:
        ret.append(record[0])
    return ret

fig = plt.figure()

ax = fig.gca(projection='3d')  

def getSnames():
    rs = cs.execute("SELECT S_NAME FROM STOCK GROUP BY S_NAME")
    ret = []
    for record in rs:
        ret.append(record[0])
    return ret 
    
    
s_names = getSnames()
# s_names = ["삼성전자","LG"]
print(s_names)

cnt = len(getPrice("삼성전자"))
x = np.zeros(cnt)
y = range(cnt)

for i,s_name in enumerate(s_names):
    z = getPrice(s_name)
    ax.plot(x+i, y, z)


plt.show()
cs.close()
conn.close()
