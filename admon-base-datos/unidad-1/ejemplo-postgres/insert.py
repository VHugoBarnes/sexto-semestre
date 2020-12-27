# coding: utf-8

# Para esta demostración, usaremos la tabla 'vendors' en la tabla 'suppliers'.
# -----------------
# |    Vendors    |
# -----------------
# |  * vendor_id  |
# |   vendor_name |
# -----------------
# 
# El método siguiente inserta una nueva fila en la tabla 'vendors' y retorna el nuevo valor generado de 'vendor_id'.

import psycopg2
from config import config # Este es el archivo que se creó primero en la presentación de powerpoint.

def insert_vendor(vendor_name):
  # Inserta un nuevo vendedor en la tabla 'vendors'.
  sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
  conn = None
  vendor_id = None
  
  try:
    # Lee la configuración de la base de datos.
    params = config()
    # Conecta con la base de datos de postgres.
    conn = psycopg2.connect(**params)
    # Crea un nuevo cursor.
    cur = conn.cursor()
    # Ejecuta el comando INSERT.
    cur.execute(sql, (vendor_name,))
    # Devuelve el id generado.
    vendor_id = cur.fetchone()[0]
    # Hace un commit a los cambios en la base de datos.
    conn.commit()
    # Cierra la comunicación con la base de datos.
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()
  
  print(vendor_id)

# El siguiente método ingresa multiples líneas en una tabla.
# Es similar a insertar una nueva linea, con la excepción de que en lugar de llamar al método
# execute(), llamamos a executemany().
def insert_vendor_list(vendor_list):
  sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
  conn = None
  try:
        # Lee la configuración de la base de datos
        params = config()
        # Connecta con la base de datos de PostgreSQL.
        conn = psycopg2.connect(**params)
        # Crea un nuevo cursor.
        cur = conn.cursor()
        # Ejecuta el comando INSERT.
        # con executemany()
        cur.executemany(sql,vendor_list)
        # Hace un commit a los cambios a la base de datos.
        conn.commit()
        # Cierra la comunicación con la base de datos.
        cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
        print(error)
  finally:
    if conn is not None:
        conn.close()
            
# Ejecución.
if __name__ == '__main__':
    # Inserta un vendedor.
    insert_vendor("3M Co.")
    # Inserta multiples vendedores.
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])