import unittest
import paramunittest
from OperateExcel import ReadExcel
# from GetMysqlData import *
from GetAPIData import *
# from tools import *
# import GetPath
# import time
import warnings

xls = ReadExcel().get_xls('user_data.xlsx', 'Regression')
area_config_id = 11
url = "https://api-ks.wtzw.com/api/v1/init-adv"


@paramunittest.parametrized(*xls)
class TestInitAdv(unittest.TestCase):
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
        if self.platform == 1:
            self.assertNotEqual(self.api_data['coopen_percent'], '')
            self.assertNotEqual(self.api_data['csj_show_privacy_dialog'], '')
            self.assertNotEqual(self.api_data['interval_time'], '')
            self.assertNotEqual(self.api_data['is_online_config'], '')
            self.assertNotEqual(self.api_data['open_percent'], '')
            self.assertNotEqual(self.api_data['total'], '')
            self.assertNotEqual(self.api_data['coopenList'], [])
            self.assertNotEqual(self.api_data['data'], [])
        else:
            pass  # 接口不同

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
