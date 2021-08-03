from flask import Flask, session, escape
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "ABCDEFG"

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/in')
def session_in():
    session["user_id"] = "s0001"
    return 'session_in'

@app.route('/del')
def session_del():
    session.pop("user_id", None)
    # session.clear()
    return 'session_del'

@app.route('/show')
def session_show():
    user_id = ""
    
    try:
        user_id = str(escape(session["user_id"]))
    except:
        pass
    
    return 'session_show : '+user_id

if __name__ == '__main__':
    app.run(debug=True)
    
