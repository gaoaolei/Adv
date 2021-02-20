import os
import GetPath
from xlrd import open_workbook
path = GetPath.get_Path()
class ReadExcel():
    def get_xls(self, xls_name, sheet_name):
        cls = []
        xlsPath = os.path.join(path, xls_name)
        file = open_workbook(xlsPath)
        sheet = file.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != 'order':   # 排除标题栏
                cls.append(sheet.row_values(i))
        return cls

if __name__ == '__main__':
    print(ReadExcel().get_xls('user_data.xlsx','dibu'))