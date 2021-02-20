import unittest
import paramunittest
from OperateExcel import ReadExcel
# from GetMysqlData import *
from GetAPIData import *
from tools import *
# import time
import warnings

xls = ReadExcel().get_xls('user_data.xlsx', 'Regression')
area_config_id = 36
url = "https://api-bc.wtzw.com/api/v1/book/download?id=151891&source=1&type=2&sign=906b54c9285a65e5f9238c8ed32cb0ca"


@paramunittest.parametrized(*xls)
class TestBookDownload(unittest.TestCase):
    """备注：表中序号好像不能用id，此处用order表示"""

    def setParameters(self, order, platform, app_version, channel, device_id, net_env, sys_ver):
        """excel见了整数，小数就是float，其他大致都是str"""
        self.order = int(order)
        self.platform = int(platform)
        self.app_version = int(app_version)
        self.channel = channel
        self.device_id = device_id
        self.net_env = int(net_env)
        self.sys_ver = sys_ver

    def setUp(self):
        """屏蔽ResourceWarning"""
        warnings.simplefilter("ignore", ResourceWarning)
        """请求接口"""
        self.api_data = get_api_data(url, self.net_env, self.channel, self.sys_ver, self.device_id, self.platform,
                                     self.app_version)

    def test_null_id(self):
        self.assertNotEqual(self.api_data['data']['id'], '')

    def test_null_link(self):
        self.assertNotEqual(self.api_data['data']['link'], '')
        self.assertTrue(self.api_data['data']['link'].endswith('zip'))

    def test_null_list(self):
        self.assertEqual(self.api_data['data']['list'], [])

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
