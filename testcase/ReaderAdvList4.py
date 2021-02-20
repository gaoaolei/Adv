import unittest
import paramunittest
from OperateExcel import ReadExcel
# from GetMysqlData import *
from GetAPIData import *
from tools import *
# import GetPath
import time
import warnings

xls = ReadExcel().get_xls('user_data.xlsx', 'InChapter')
area_config_id = 30
url = "https://api-ks.wtzw.com/api/v1/reader-adv"


@paramunittest.parametrized(*xls)
class TestAdvInChapter(unittest.TestCase):
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
        """忽略ResourceWarning"""
        warnings.simplefilter('ignore', ResourceWarning)
        """获取数据库数据"""

        """有报错，先注释掉"""
        # advs = get_mysql_data(self.device_id, area_config_id, self.platform, self.app_version)
        advs = []
        self.gaojia = []
        self.dijia = []
        if advs != []:
            for adv in advs:
                id = adv[0]
                # area_config_id = adv[1]  # 放开会报错
                title = adv[2]
                price_type = adv[3]
                content = adv[4]
                advertiser = adv[5]
                adv_style = adv[6]
                adv_type = adv[7]
                adv_code = adv[8]
                platform = adv[9]
                app_type = adv[10]
                gender = adv[11]
                show_percent = adv[12]
                statistical_code = adv[13]
                begin_time = adv[14]
                end_time = adv[15]
                min_app_version = adv[16]
                max_app_version = adv[17]
                allow_channel = adv[18]
                deny_channel = adv[19]
                image = adv[20]
                link = adv[21]
                order = adv[22]
                json_data = adv[23]
                status = adv[24]
                show_time = adv[25]
                show_frequency = adv[26]
                ab_group_id = adv[27]
                adv_backend_id = adv[28]
                created_at = adv[29]
                updated_at = adv[30]

                json_data_dict = json.loads(json_data)
                form_type = json_data_dict.get('form_type', '0')
                sort = json_data_dict.get('sort', '')
                multi_level = json_data_dict.get('multi_level', '0')
                multi_level_sort = json_data_dict.get('multi_level_sort', '')
                # network_env = json_data_dict.get('network_env','0')
                # ....---------------------------其他用到再添加进来---------------------

                online_form_type = zhangnei_form_type(self.app_version, area_config_id, self.platform)
                if form_type == online_form_type:
                    flag = channel_filter(allow_channel, deny_channel, self.channel)
                    if flag == False:
                        if price_type == 1:
                            if (sort != '' and multi_level == '0') or (
                                                sort != '' and multi_level == '1' and multi_level_sort != ''):
                                self.gaojia.append(adv)
                        else:
                            if int(show_percent) != 0:
                                self.dijia.append(adv)
                else:
                    print('不符合条件')

        """获取接口数据"""
        response = get_api_data(url, self.net_env, self.channel, self.sys_ver, self.device_id, self.platform,
                                self.app_version)
        self.api_data = response['data']['list4']
        return self.gaojia, self.dijia, self.api_data

    @unittest.skip
    def test_001_compare_gajia_order(self):
        """获取数据库数据排序后的高价代码位"""
        # 新版本根据network_env区分数据
        gaojia_net = []
        if (self.app_version >= 40060 and self.platform == 1) or (self.app_version >= 3030000 and self.platform == 2):
            for i in self.gaojia:
                if self.net_env == 1:
                    if json.loads(i[23])['network_env'] == '1':
                        gaojia_net.append(i)
                else:
                    if json.loads(i[23])['network_env'] == '2':
                        gaojia_net.append(i)
            self.gaojia = gaojia_net
        print(gaojia_net)

        self.gaojia.sort(
            key=lambda element: (json.loads(element[23])['sort'], json.loads(element[23])['multi_level_sort']))
        adv_code_gaojia_mysql = []
        for i in self.gaojia:
            adv_code_gaojia_mysql.append(i[8])
        # 根据网路环境返不同的id
        # if self.app_version >= 40060 and self.platform == 1:
        #     adv_code_gaojia_mysql = net(adv_code_gaojia_mysql, self.net_env)


        # 获取接口数据排序后的高价代码位
        adv_code_gaojia_api = []
        for i in self.zhangneiadv:
            if i['price_type'] == '1':
                adv_code_gaojia_api.append(i['adv_code'])

        print('code_mysql:', adv_code_gaojia_mysql)
        print('code_api:', adv_code_gaojia_api)

        # 自己判断后写结果
        if adv_code_gaojia_mysql != adv_code_gaojia_api:
            content = '%s  章内%s用例失败，数据库结果为%s,接口结果为%s\n' % (
                time.ctime(), self.order, adv_code_gaojia_mysql, adv_code_gaojia_api)
            write_result(content)

        # 生成报告用
        self.assertEqual(adv_code_gaojia_mysql, adv_code_gaojia_api)

    @unittest.skip
    def test_002_compare_content(self):

        list2 = []

        ab_data = get_abgroup_data(self.device_id, area_config_id, self.platform, self.app_version)
        print('adav_ab数据：')
        print(ab_data)

        self.gaojia.sort(
            key=lambda element: (json.loads(element[23])['sort'], json.loads(element[23])['multi_level_sort']))
        print('adv数据：')
        print(self.gaojia)
        for adv in self.gaojia:
            id = adv[0]
            # area_config_id = adv[1]  # 放开会报错
            title = adv[2]
            price_type = adv[3]
            content = adv[4]
            advertiser = adv[5]
            adv_style = adv[6]
            adv_type = adv[7]
            adv_code = adv[8]
            platform = adv[9]
            app_type = adv[10]
            gender = adv[11]
            show_percent = adv[12]
            statistical_code = adv[13]
            begin_time = adv[14]
            end_time = adv[15]
            min_app_version = adv[16]
            max_app_version = adv[17]
            allow_channel = adv[18]
            deny_channel = adv[19]
            image = adv[20]
            link = adv[21]
            order = adv[22]
            json_data = adv[23]
            status = adv[24]
            show_time = adv[25]
            show_frequency = adv[26]
            ab_group_id = adv[27]
            adv_backend_id = adv[28]
            created_at = adv[29]
            updated_at = adv[30]
            json_data_dict = json.loads(json_data)
            sort = json_data_dict.get('sort', '')
            multi_level = json_data_dict.get('multi_level', '0')
            multi_level_sort = json_data_dict.get('multi_level_sort', '')
            # ....---------------------------其他用到再添加进来---------------------

            dict = {}
            dict['ab_group'] = ab_data['index']
            dict['ab_group_id'] = ab_data['group_id']
            dict['ab_statistical_code'] = ab_data['statistical_code']
            dict['id'] = id
            # --------继续加---------
            list2.append(dict)
        print('-----------')
        print(list2)
        print(json.dumps(list2, indent=True))

    def test_null_list4(self):
        self.assertNotEqual(self.api_data, [])

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
