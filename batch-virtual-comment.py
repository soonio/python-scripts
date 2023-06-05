import time
import xlrd

# 读取xlsx文件
# wb = xlrd.open_workbook('/Users/qingliu/Desktop/1.xlsx')
wb = xlrd.open_workbook('/Users/qingliu/Desktop/批量评论0605.xls')
# 获取工作表
sheet = wb.sheet_by_name('Sheet1')
# 获取单元格数据

row = 1
while row < sheet.nrows:
    id = sheet.cell_value(row, 0)
    uid = sheet.cell_value(row, 1)
    typ = sheet.cell_value(row, 2)
    content = sheet.cell_value(row, 3)
    anonymous = sheet.cell_value(row, 5)
    created = sheet.cell_value(row, 7)

    if isinstance(created, float):
        q = str(xlrd.xldate_as_datetime(created, 0))
        t = int(time.mktime(time.strptime(q, "%Y-%m-%d %H:%M:%S")))
    else:
        t = int(time.mktime(time.strptime(created, "%Y/%m/%d %H:%M:%S")))

    r = "({id}, {uid}, {type}, '{content}', 1, {anonymous}, 1, {created}, {created}),".format(
        id=int(id),
        uid=int(uid),
        type=int(typ[0]),
        content=content,
        anonymous=int(anonymous),
        created=t)
    print(r)

    row += 1

# python batch-virtual-comment.py > part.sql
