import cx_Oracle
import mybatis_mapper2sql
from day22survey.mylog import MyLog

class MyDaoSuser:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@localhost:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0]
        
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'user_id':record[0],'pwd':record[1],'user_name':record[2],'mobile':record[3],'email':record[4],'birth':record[5],'in_date':record[6],'in_user_id':record[7],'up_date':record[8],'up_user_id':record[9]})
        return list
    
    
    def myinsert(self,user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (user_id, pwd, user_name, mobile, email, birth, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,user_id, pwd, user_name, mobile, email, birth, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")       
        self.cs.execute(sql, (pwd, user_name, mobile, email, birth, up_user_id,user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def mydelete(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete") 
        self.cs.execute(sql, (user_id,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoSuser()

    
    
    