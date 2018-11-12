# #coding:utf-8
# #Author:sgao
import xlrd
import json
# def getreaddata(file_name):
#     file_d = xlrd.open_workbook(file_name)
#     # 获得第一个页签对象
#     select_sheet = file_d.sheets()[0]
#
#     machineId = []
#     machineCode = []
#     # 获取总共的行数
#     rows_num = select_sheet.nrows
#     # 得到行数
#     # print rows_num
#
#     for row in xrange(rows_num):
#         first_id = select_sheet.cell(row, 0).value
#         first_code = select_sheet.cell(row,1).value
#         machineId.append(first_id)
#         machineCode.append(first_code)
#
#     # print machineCode
#     # print machineId
#
#     return json.dumps(list(zip(machineCode,machineId)))
#
# # [{"machineCode":"18047652","machineId":"5d80295b4b144fbbb55b15e6d1f22ac0"},
# # {"machineCode":"18136238","machineId":"2bfcfe7184f84a5597bbfca9d9781574"}]
#
#
# result = []
#
# a = getreaddata('testexcel.xls')
#
# b = json.loads(a)
# # print(type(b))
# for item in b:
#
#     c = {"machineCode": item[0], "machineId": item[1]}
#     # print(c)
#     # print(type(c))
#     result.append(c)
#     # print item
#     # print type(item)
#     # for item2 in item:
#     #     print item2
#
# print(result)
# for i in range(len(result)):
#     print type(result[i]['machineCode'])
#
# # for item in a:
# #     print(type(item))
#
#
#

import xlrd
import json
import xlwt

# print type(machineId)
# def getcode(file_name):
#     file_d = xlrd.open_workbook(file_name)
#     # 获得第一个页签对象
#     select_sheet = file_d.sheets()[0]
#
#     machineCode = []
#     # 获取总共的行数
#     rows_num = select_sheet.nrows
#     # 得到行数
#     # print rows_num
#
#     for row in xrange(rows_num):
#         first_code = select_sheet.cell(row, 0).value
#         machineCode.append(first_code)
#
#     return machineCode
#
#
# data = getcode('sjiqi.xls')
# print type(data)
#
# pass_arr = ['123','345']
# false_arr = ['999','888']
# def write(file_name,passdata,failedata):
#     book = xlwt.Workbook()
#     #创建excel对象
#     sheet = book.add_sheet('sheet1')
#     # for i,p in enumerate(data):
#     #     print p
#     #     for j,q in enumerate(p):
#     #         # print i,j,p
#     #         sheet.write(i,j,p)
#     for i in range(0,len(passdata)):
#         # 成功放入第2列
#         sheet.write(i,1,passdata[i])
#     for i in range(0,len(failedata)):
#         # 失败放入第1列
#         sheet.write(i,0,failedata[i])
#
#     book.save(file_name)
#
#
# write('resultdata.xls',pass_arr,false_arr)


def getauto(file_name):
    file_d = xlrd.open_workbook(file_name)
    # 获得第一个页签对象
    select_sheet = file_d.sheets()[0]

    machineCode = []
    machineCode2 = ""
    # 获取总共的行数
    rows_num = select_sheet.nrows
    # 得到行数
    # print rows_num

    for row in xrange(rows_num):
        first_code = select_sheet.cell(row,0).value
        machineCode.append(first_code)
        # machineCode2=machineCode2+","+first_code


    print json.dumps(machineCode)
    print machineCode2



# getauto('machine1031_1002.xls')



def getcatapp(file_name):
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

    return  json.dumps(dict(zip(machineCode, machineId)))

# getcatapp('machine1031_1002.xls')


machineId1 = {"0020f614256d4a0c95619b10805533e8":'123', "00b0965295f2427f8f45978d8e345762":'45566'}
for key in machineId1:
    a = key
    b = machineId1[key]
    print a
    print b
