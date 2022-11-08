import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='mydb',
                     charset='utf8')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print(data)

print("connect successful !")

db.close()