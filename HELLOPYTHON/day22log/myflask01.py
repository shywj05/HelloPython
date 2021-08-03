from flask import Flask
from day22log.mylog import MyLog

mylog = MyLog()

app = Flask(__name__)

@app.route('/h1')
def h1():
    sql = "11111"
    mylog.logger.debug(sql)
   
    return 'h1'

@app.route('/h2')
def h2():
    sql = "22222"
    mylog.logger.debug(sql)
   
    return 'h2'

if __name__ == '__main__':
    app.run(debug=True)
    
    