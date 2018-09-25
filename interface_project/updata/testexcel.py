#coding:utf-8
#Author:sgao
import xlrd
import json
def getreaddata(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineId = []
    machineCode = []
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_id = select_sheet.cell(row, 0).value
        first_code = select_sheet.cell(row,1).value
        machineId.append(first_id)
        machineCode.append(first_code)

    # print machineCode
    # print machineId

    return json.dumps(list(zip(machineCode,machineId)))

# [{"machineCode":"18047652","machineId":"5d80295b4b144fbbb55b15e6d1f22ac0"},
# {"machineCode":"18136238","machineId":"2bfcfe7184f84a5597bbfca9d9781574"}]


result = []

a = getreaddata('testexcel.xls')

b = json.loads(a)
# print(type(b))
for item in b:

    c = {"machineCode": item[0], "machineId": item[1]}
    # print(c)
    # print(type(c))
    result.append(c)
    # print item
    # print type(item)
    # for item2 in item:
    #     print item2

print(result)
for i in range(len(result)):
    print type(result[i]['machineCode'])

# for item in a:
#     print(type(item))



