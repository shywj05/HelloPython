from flask import Flask, render_template, jsonify, request
import cx_Oracle
from day22survey.mydao_suser import MyDaoSuser
from day22survey.mydao_survey import MyDaoSurvey
from day22survey.mydao_detail import MyDaoDetail


app = Flask(__name__, static_url_path="", static_folder="static")

@app.route("/suser")
def suser_render():
    list = MyDaoSuser().myselect()
    return render_template('suser.html', list=list)

@app.route('/suser_ins.ajax', methods=['POST'])
def suser_ins_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]

    cnt = MyDaoSuser().myinsert(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/suser_upd.ajax', methods=['POST'])
def suser_upd_ajax():
    user_id = request.form["user_id"]
    pwd = request.form["pwd"]
    user_name = request.form["user_name"]
    mobile = request.form["mobile"]
    email = request.form["email"]
    birth = request.form["birth"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDaoSuser().myupdate(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/suser_del.ajax', methods=['POST'])
def suser_del_ajax():
    user_id = request.form["user_id"]

    cnt = MyDaoSuser().mydelete(user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

########################### SURVEY ############################################################

@app.route("/survey")
def survey_render():
    list = MyDaoSurvey().myselect()
    return render_template('survey.html', list=list)

@app.route('/survey_ins.ajax', methods=['POST'])
def survey_ins_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    a2 = request.form["a2"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]

    cnt = MyDaoSurvey().myinsert(survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/survey_upd.ajax', methods=['POST'])
def survey_upd_ajax():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    a2 = request.form["a2"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDaoSurvey().myupdate(survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/survey_del.ajax', methods=['POST'])
def survey_del_ajax():
    survey_id = request.form["survey_id"]

    cnt = MyDaoSurvey().mydelete(survey_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

############################# DETAIL ##########################################################

@app.route("/detail")
def detail_render():
    list = MyDaoDetail().myselect()
    return render_template('detail.html', list=list)

@app.route('/detail_ins.ajax', methods=['POST'])
def detail_ins_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]

    cnt = MyDaoDetail().myinsert(survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/detail_upd.ajax', methods=['POST'])
def detail_upd_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]
    question = request.form["question"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    a4 = request.form["a4"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    cnt = MyDaoDetail().myupdate(survey_id, s_seq, question, a1, a2, a3, a4, in_date, in_user_id, up_date, up_user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route('/detail_del.ajax', methods=['POST'])
def detail_del_ajax():
    survey_id = request.form["survey_id"]
    s_seq = request.form["s_seq"]

    cnt = MyDaoDetail().mydelete(survey_id, s_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)



if __name__ == "__main__":
    app.run(debug=True)


