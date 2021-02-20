import os
# 给出项目的根目录
def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__  == '__main__':
    print('根路径为：', get_Path())