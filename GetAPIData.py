from tools import *
from OperateAPI import APIData


#   ---------------header 里的9 需要处理---------------
def get_api_data(url, net_env, channel, sys_ver, device_id, platform, app_version):

    # headers中1--android，2--ios
    if platform == 1:
        platform_tmp = 'android'
    else:
        platform_tmp = 'ios'
    header = get_headers(net_env, channel, sys_ver, device_id, platform_tmp, app_version)

    response = APIData().getdata(url, header)

    return response


if __name__ == '__main__':
    # url = "http://172.16.100.61:8301/api/v1/reader-adv"
    url = "https://api-ks.wtzw.com/api/v1/reader-adv"
    device_id = '20190712141352c5590aeffbbec19d7b474f3958f971c8018c311326c075ea'
    a = get_api_data(url, 1, 'unknown', 9, device_id, 1, 40100 )
    print(a)
