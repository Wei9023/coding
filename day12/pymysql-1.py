import pymysql

conn = pymysql.connect(host='192.168.0.6', port=3306, user='root',
                       passwd='tonys-air', db='vvtestdb')

cursor = conn.cursor()

#effect_row = cursor.execute('select * from student')
#print(cursor.fetchall())

data = [
    ("N1",21,"2015-05-22",'M'),
    ("N2",20,"2015-05-21",'M'),
    ("N3",21,"2015-05-23",'F'),
]

cursor.executemany("insert into student (name,age,register_date,gender) values(%s,%s,%s,%s)", data)

conn.commit()
