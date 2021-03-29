#用于获取excel文件里面的测试数据,就是测试用例
import xlrd
def get_excel():
    rows_list = []
    excel = xlrd.open_workbook('../testdata/data.xlsx')  #通过相对路径打开excel文件
    table = excel.sheets()[0] #获取第一张表格
    # print(table.nrows)
    # print(table.ncols)
    # print(table.row_values(1))
    # print(table.col_values(1))
    # print(table.nrows)
    for row in range(1,table.nrows):
        rows_list.append((table.cell_value(row,1), table.cell_value(row,2), table.cell_value(row,3), table.cell_value(row,4), table.cell_value(row,5)))
    # return table.cell_value(row,1), table.cell_value(row,2) #通过行返回2、3列的数据
    # print(rows_list)
    return rows_list

    # print(table.cell_value(0,0)) #table.cell_value(row,col),(行，列)
if __name__ == '__main__':
    print(get_excel())#返回第二行数据