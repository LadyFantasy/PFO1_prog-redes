import sqlite3
from datetime import datetime



def db_initialize():
    try:
        
        conexion = sqlite3.connect('messages.db')
        cursor = conexion.cursor() 
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                contenido TEXT NOT NULL,              
                fecha_envio TEXT NOT NULL,              
                ip_cliente TEXT NOT NULL               
            )
        ''')
        
        conexion.commit()  
        conexion.close()   
        return True
    except sqlite3.Error as e:
        
        print(f"No se puede iniciar la base de datos: {e}")
        return False


def save_msg(contenido, ip_cliente):
    try:
        conection = sqlite3.connect('messages.db')  
        cursor = conection.cursor()
        
        fecha_envio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
       
        cursor.execute('''
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        ''', (contenido, fecha_envio, ip_cliente))
        
        conection.commit() 
        conection.close()   
        
        return fecha_envio  
    except sqlite3.Error as e:
        print(f"Error al guardar mensaje: {e}")



