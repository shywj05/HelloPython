from flask import Flask
import logging



formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('sample')
logger.setLevel(logging.DEBUG)

    
ch = logging.StreamHandler()
ch.setFormatter(formatter)
fh = logging.FileHandler(filename="run.log")
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


app = Flask(__name__)

@app.route('/h1')
def h1():
    sql = "11111"
    logger.debug(sql)
   
    return 'h1'

@app.route('/h2')
def h2():
    sql = "22222"
    logger.debug(sql)
   
    return 'h2'



if __name__ == '__main__':
    app.run(debug=True)
    
    