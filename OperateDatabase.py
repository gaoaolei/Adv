import mysql.connector
import json
host = '172.16.100.80'
port = '3306'
user = 'qimao_free_test'
password = 'd3R6d190ZXN0Cg=='
database = 'free_ad'
conn = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
cursor = conn.cursor(dictionary=False)


class MysqlData(object):
    # 数据库查询
    def getdata(self, query_sql, params=None):
        cursor.execute(query_sql, params)
        data = cursor.fetchall()
        return data

if __name__ == '__main__':
    sql = "SELECT * FROM adv WHERE area_config_id=11 AND platform=1 AND STATUS=1 AND min_app_version=40060 AND ab_group_id='' AND adv_code !='' "
    test = MysqlData()
    test = test.getdata(sql)
    print(test)
    print(type(test))
    for i in test:
        print(i)
        print(type(i))
        print(i['json_data'])
        print(type(i['json_data']))



