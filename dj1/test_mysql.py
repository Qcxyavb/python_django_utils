import pymysql


db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='mydb',
                     charset='utf8')

cursor = db.cursor()

# cursor.execute("select version()")
#
# data = cursor.fetchone()

# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
#
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 执行sql语句
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# 查询表头
# select column_name from Information_schema.columns where table_Name = 'ali_pay_bill_detail_demo'


sql = "SELECT * FROM ali_pay_bill_detail_demo \
       WHERE id < %s" % (115666)


try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
       for column in (0,len(row)+1):
           print(row[column])
            # fname = row[0]
            # lname = row[1]
            # age = row[2]
            # sex = row[3]
            # income = row[4]
       # 打印结果
       #      print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
       #       (row[column], lname, age, sex, income ))
except:
   print ("Error: unable to fetch data")


print("connect successful !")

db.close()