import pymysql
from config.conf import *

def get_mysql(sql):
    host, user, password, port, database, charset=sql_conf()
    conn = pymysql.connect(host=host,user=user,password=password,port=port,database=database,charset=charset)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

if __name__ == '__main__':
    sql = "select * from users where `id`=1;"
    print(get_mysql(sql))
