import pymysql.connections

db = pymysql.connect(host='localhost',user='root',password='kekokaka',db='escuela')

cursor = db.cursor()

sql = "INSERT INTO alumnos (idalumnos, Salon, Nombre) VALUES (%s, %s, %s)"
val = (17260620,"3A", "Nicole")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")