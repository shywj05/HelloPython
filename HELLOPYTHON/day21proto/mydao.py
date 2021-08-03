import cx_Oracle
import mybatis_mapper2sql

class MyDao:
    def __init__(self): 
        self.conn = cx_Oracle.connect("python/python@localhost:1521/xe")
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_sample.xml')[0]
        
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'col01': record[0], 'col02':record[1], 'col03': record[2]})
        return list
    
    def myinsert(self, col01, col02, col03):
        
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql,(col01, col02, col03))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def myupdate(self, col01, col02, col03):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        self.cs.execute(sql,(col02, col03, col01))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def mydelete(self, col01):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        self.cs.execute(sql,(col01,))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        cnt = self.cs.rowcount
        return cnt


if __name__ == '__main__':
    dao = MyDao()
#     list = dao.myselect()
#     print(list)
    list = dao.myinsert(10, 8, 8)
    print(list)
    
#     list = dao.myupdate(7, 10, 10)
#     list = dao.mydelete(4)
    
    

