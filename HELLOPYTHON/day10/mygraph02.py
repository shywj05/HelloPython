import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import cx_Oracle
import numpy as np

def getPrice(S_NAME):
    conn=cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    rs = cs.execute("SELECT S_PRICE FROM STOCK WHERE S_NAME = '"+S_NAME+"' ORDER BY S_INTIME")

    ret = []
    for record in rs:
        ret.append(record[0])
    
    cs.close()
    conn.close()
    return ret

fig = plt.figure()

ax = fig.gca(projection='3d')  



s_names = ["삼성전자","LG","현대차","기아차"]
cnt = len(getPrice("삼성전자"))

x = np.zeros(cnt)
y = range(cnt)

for i,s_name in enumerate(s_names):
    z = getPrice(s_name)
    ax.plot(x+i, y, z)

# z = getPrice(s_names[0]) #소스를 깨끗하게 하기 위해 메소드로 연결하여 부른다.
# ax.plot(x, y, z) 
# 
# z = getPrice(s_names[1])
# ax.plot(x+1, y, z) 
# 
# z = getPrice(s_names[2])
# ax.plot(x+2, y, z) 

plt.show()
