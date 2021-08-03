import cx_Oracle
import mybatis_mapper2sql

class suserdao:
    def __init__(self): 
        self.conn = cx_Oracle.connect("python/python@localhost:1521/xe")
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_suser.xml')[0]
        
    def suser_myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'user_id': record[0], 'pwd':record[1], 'user_name': record[2], 'mobile': record[3], 'email': record[4], 'birth': record[5], 'in_date': record[6], 'in_user_id': record[7], 'up_date': record[8], 'up_user_id': record[9]})
        return list
    
    def suser_myinsert(self, user_id, pwd, user_name,mobile,email,birth,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql,(user_id, pwd, user_name,mobile,email,birth,in_date,in_user_id,up_date,up_user_id))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def suser_myupdate(self, user_id, pwd, user_name,mobile,email,birth,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        self.cs.execute(sql,(user_id, pwd, user_name,mobile,email,birth,in_date,in_user_id,up_date,up_user_id))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def suser_mydelete(self, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        self.cs.execute(sql,(user_id,))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        cnt = self.cs.rowcount
        return cnt


#     print(list)
#     list = dao.myinsert(10, 8, 8)
#     print(list)
    
#     list = dao.myupdate(7, 10, 10)
#     list = dao.mydelete(4)
    
    

