from flask import Flask, render_template, jsonify, request
import cx_Oracle
from day21survey.surveydao import surveydao
from day21survey.suserdao import suserdao


def suser_getData():
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    rs = cs.execute("select user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id from suser")
    
    list = []
    
    for record in rs:
        list.append({'user_id': record[0], 'pwd':record[1], 'user_name': record[2], 'mobile': record[3], 'email': record[4], 'birth': record[5], 'in_date': record[6], 'in_user_id': record[7], 'up_date': record[8], 'up_user_id': record[9]})
        
    cs.close()
    conn.close()
    
    return list


def suser_myinsert(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    sql = "insert into suser(user_id, pwd, user_name, mobile, email, birth,in_date, in_user_id, up_date, up_user_id) values (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)"
    cs.execute(sql, (user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id))
    cnt = cs.execute
    print(cs.rowcount)
    
    conn.commit()    
    cs.close()
    conn.close()
    

def suser_myupdate(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    sql = "update suser set pwd=:1, user_name=:2, mobile=:3, email=:4, birth=:5, in_date=:6, in_user_id=:7, up_date=:8, up_user_id=:9 where user_id=:10"
    cs.execute(sql, (pwd, user_name, mobile,email,birth,in_date,in_user_id,up_date,up_user_id,user_id))
    cnt = cs.rowcount
    
    conn.commit()    
    cs.close()
    conn.close()    
    
    return cnt

    
def suser_mydelete(user_id):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")

    cs = conn.cursor()
    sql = "delete from suser where user_id=:1"
    cs.execute(sql, (user_id,))
    cnt = cs.rowcount
    
    conn.commit()    
    cs.close()
    conn.close()
    
    return cnt


app = Flask(__name__, static_url_path="", static_folder='static')


@app.route('/suser')
def suser_render():
    list = suser_getData()
        
    return render_template('suser.html', list=list)


@app.route('/suser_ins.ajax', methods=['post'])
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
    cnt = suserdao().suser_myinsert(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)

    
@app.route('/suser_upd.ajax', methods=['post'])
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
    cnt = suserdao().suser_myupdate(user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)

    
@app.route('/suser_del.ajax', methods=['post'])
def suser_del_ajax():
    user_id = request.form["user_id"]
    cnt = suserdao().suser_mydelete(user_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)
    print(user_id)

################################################################################################################################

def survey_getData():
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    rs = cs.execute("select survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id from survey")
    
    list = []
    
    for record in rs:
        list.append({'survey_id': record[0], 'title':record[1], 'content': record[2], 'interview_cnt': record[3], 'a2': record[4], 'in_date': record[5], 'in_user_id': record[6], 'up_date': record[7], 'up_user_id': record[8]})
        
    cs.close()
    conn.close()
    
    return list


def survey_insert(survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    sql = "insert into survey(survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)"
    cs.execute(sql, (survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id))
    cnt = cs.execute
    print(cs.rowcount)
    
    conn.commit()    
    cs.close()
    conn.close()
    

def survey_update(title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id, survey_id, ):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")
    cs = conn.cursor()
    sql = "update survey set title=:1, content=:2, interview_cnt=:3, a2=:4, in_date=:5, in_user_id=:6, up_date=:7, up_user_id=:8 where survey_id=:9"
    cs.execute(sql, (title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id, survey_id))
    cnt = cs.rowcount
    
    conn.commit()    
    cs.close()
    conn.close()    
    
    return cnt

    
def survey_delete(survey_id):
    conn = cx_Oracle.connect("python/python@localhost:1521/xe")

    cs = conn.cursor()
    sql = "delete from survey where survey_id=:1"
    cs.execute(sql, (survey_id,))
    cnt = cs.rowcount
    
    conn.commit()    
    cs.close()
    conn.close()
    
    return cnt


app = Flask(__name__, static_url_path="", static_folder='static')


@app.route('/survey')
def survey_render():
    list = survey_getData()
        
    return render_template('survey.html', list=list)


@app.route('/survey_ins.ajax', methods=['post'])
def survey_ins():
    survey_id = request.form["survey_id"]
    title = request.form["title"]
    content = request.form["content"]
    interview_cnt = request.form["interview_cnt"]
    a2 = request.form["a2"]
    in_date = request.form["in_date"]
    in_user_id = request.form["in_user_id"]
    up_date = request.form["up_date"]
    up_user_id = request.form["up_user_id"]
    
    cnt = surveydao().survey_myinsert(survey_id, title, content, interview_cnt, a2, in_date, in_user_id, up_date, up_user_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)

    
@app.route('/survey_upd.ajax', methods=['post'])
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
    cnt = surveydao().survey_myupdate(survey_id, title, content, interview_cnt, a2, in_date,in_user_id,up_date,up_user_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)

    
@app.route('/survey_del.ajax', methods=['post'])
def survey_del_ajax():
    survey_id = request.form["survey_id"]
    cnt = surveydao().survey_mydelete(survey_id)
    msg = ""
    if cnt == 1:
        msg = 'ok'
    else:
        msg = 'ng'
        
    return jsonify(msg=msg)
    print(survey_id)


if __name__ == '__main__':
    app.run(debug=True)
    
    
