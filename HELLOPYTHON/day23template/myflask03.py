from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder="static")

@app.route('/suser')
def suser():
    return render_template('suser.html')
@app.route('/survey')
def survey():
    return render_template('survey.html')
@app.route('/sdetail')
def detail():
    return render_template('sdetail.html')

if __name__ == '__main__':
    app.run(debug=True)
    