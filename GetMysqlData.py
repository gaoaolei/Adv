from tools import *


def get_mysql_data(device_id, area_config_id, platform, app_version):
    advs = []
    is_vip_flag = is_vip('token')
    if is_vip_flag == True:
        return advs
    sql_data = sql(device_id, area_config_id, platform, app_version)
    advs = MysqlData().getdata(sql_data[0], sql_data[1])
    return advs

if __name__ == '__main__':
    device_id = '20190712141352c5590aeffbbec19d7b474f3958f971c8018c311326c075ef'
    res = get_mysql_data(device_id, 30, 1, 40100)
    print(res)