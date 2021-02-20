import GetPath
import os
import unittest
import ConfigEmail
from HTMLTestRunner import HTMLTestRunner
from tools import *

path = GetPath.get_Path()


class AllTest(object):
    def __init__(self):
        self.caseSuite = []
        self.caseName = ''
        self.caseFilePath = os.path.join(path, 'testCase')
        self.caseListFile = os.path.join(path, 'caselist.txt')
        self.path = ''

    def set_case_suite(self):
        fb = open(self.caseListFile, 'r')
        for value in fb.readlines():
            data = str(value)
            """获取需要执行的用例py文件名"""
            if data != '' and not data.startswith('#'):
                self.caseName = data.replace('\n', '')
                """将py文件添加到testSuite中"""
                discover = unittest.defaultTestLoader.discover(self.caseFilePath, pattern=self.caseName, top_level_dir=None)
                self.caseSuite.append(discover)
        fb.close()
        return self.caseSuite

    def run(self):
        """执行用例"""
        result = os.path.join(GetPath.get_Path(), 'result', 'report.html')
        with open(result, 'wb') as f:
            runner = HTMLTestRunner(stream=f,
                                    title='广告接口测试结果',
                                    description='以下为七猫免费小说广告接口测试结果清单',
                                    verbosity=2)
            runner.run(unittest.TestSuite(self.set_case_suite()))

        '''执行时打印输出，不生成报告'''
        # unittest.TextTestRunner().run(unittest.TestSuite(self.set_case_suite()))

        """发送邮件"""
        self.path = os.path.join(GetPath.get_Path(), r'result\report.html')
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    """找到结论行，取出结果发邮件"""
                    if '<strong>Status:</strong>' in line and 'Failure' in line:
                        content = line.split('<')[3].split('>')[1]
                        ConfigEmail.send_mail(content)
                        break
        else:
            print("报告不存在")

        # self.path = os.path.join(GetPath.get_Path(), r'result\result.txt')
        # if os.path.exists(self.path):
        #     with open(self.path, 'r', encoding='utf-8') as f:
        #         content = f.read()
        #         ConfigEmail.send_mail(content)
        #     """删除result.txt,为下次做准备"""
        #     os.remove(self.path)


if __name__ == '__main__':
    AllTest().run()




