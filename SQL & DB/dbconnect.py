import mysql.connector
import pandas as pd
import numpy as np

## 資料庫連線
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='',  # 自己填入資料庫密碼
    database='baseball_db'
)

mycursor = db.cursor(buffered=True)

"""
## key in data

df = pd.read_csv("clean")
name_li = df['player']
value_li = df['value']
year_li = df['draft year']

for idx in range(0, len(name_li)):
    sql = "INSERT INTO `contract` (`temp_order`,`name`, `value`, `year`) VALUES (%s, %s, %s, %s)"
    val = (idx, str(name_li[idx]), str(value_li[idx]), str(year_li[idx]))
    mycursor.execute(sql, val)
    db.commit()
"""



"""
## 取出資料

sql = "SELECT * from contract WHERE name = 'Dwight Gooden'"
mycursor.execute(sql)

result= mycursor.fetchall()

for i in result:
    print(i)
"""

"""
## 結果：
(5908, 'Dwight Gooden', '15450000', '1982')
(5909, 'Dwight Gooden', '6700000', '1982')
(5910, 'Dwight Gooden', '5675000', '1982')
(5911, 'Dwight Gooden', '1400000', '1982')
(5912, 'Dwight Gooden', '1400000', '1982')
(5913, 'Dwight Gooden', '1320000', '1982')
(5914, 'Dwight Gooden', '850000', '1982')
(5915, 'Dwight Gooden', '500000', '1982')
(5916, 'Dwight Gooden', '275000', '1982')
(5917, 'Dwight Gooden', '85000', '1982')
(5918, 'Dwight Gooden', '40000', '1982')
"""

## 取消資料庫連線
mycursor.close()

