from flask import Flask, render_template

app = Flask(__name__)

@app.route('/render')
def render():
    list = ["홍길동","전우치","이순신"]
    
    return render_template('myflask.html', data_list=list, str="이순신짱")

if __name__ == '__main__':
    app.run(debug=True)
    