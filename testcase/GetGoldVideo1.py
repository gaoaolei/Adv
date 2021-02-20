import unittest
import paramunittest  # 将Excel表的字段变成类的属性
from OperateExcel import ReadExcel
# from GetMysqlData import *
from GetAPIData import *
# from tools import *
# import GetPath
# import time
import warnings

xls = ReadExcel().get_xls('user_data.xlsx', 'Regression')
url = "https://api-ks.wtzw.com/api/v1/get-gold-video?type=1&apiVersion=20190309143259-1.9&t=1612712265615"


@paramunittest.parametrized(*xls)
class TestGoldVideo1(unittest.TestCase):
    def setParameters(self, order, platform, app_version, channel, device_id, net_env, sys_ver):
        self.order = int(order)
        self.platform = int(platform)
        self.app_version = int(app_version)
        self.channel = channel
        self.device_id = device_id
        self.net_env = int(net_env)
        self.sys_ver = sys_ver

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        """获取接口数据"""
        self.api_data = get_api_data(url, self.net_env, self.channel, self.sys_ver, self.device_id, self.platform,
                                     self.app_version)

    def test_null(self):
        self.assertNotEqual(self.api_data['data'], '')
        self.assertNotEqual(self.api_data['data']['gold_video'], '')
        self.assertNotEqual(self.api_data['data']['noad_video'], '')
        self.assertNotEqual(self.api_data['data']['sign'], '')
        self.assertNotEqual(self.api_data['data']['small_video'], '')

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
