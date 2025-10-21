import mysql.connector
from mysql.connector import errorcode
cursor = None
cnx = None

def ConectarBase():
    global cursor, cnx
    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="gestion_db")
        cursor = cnx.cursor(dictionary=True)
        print('Conexión establecida')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)

def ConsultaSelect():
    Consulta = "SELECT * FROM clientes;"
    cursor.execute(Consulta)
    return cursor.fetchall()

def ConsultaInsertar(nombre, dni, correo, saldo):
    sql = "INSERT INTO clientes (nombre, dni, correo, saldo)VALUES( %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, dni, correo, saldo))
    cnx.commit()
    return cursor.lastrowid

ConectarBase()
ConsultaInsertar("pesdsaasd", 94975861, "roberto@gmail.com", 500.00)
print(ConsultaSelect())
if cnx.is_connected():
    cnx.close()
    print("La conexión a la base de datos ha sido cerrada.")
