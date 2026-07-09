import psycopg2  # La herramienta profesional para hablar con Postgres

print("--- CONECTANDO AL ALMACÉN PROFESIONAL (POSTGRES) ---")

try:
    # 1. Nos conectamos al servidor de Postgres usando tus credenciales
    conexion = psycopg2.connect(
        host="localhost",
        database="mi_empresa_pro",
        user="postgres",
        password="SAMA980109MU1$"  # <-- ¡Pon aquí tu contraseña real!
    )
    
    cursor = conexion.cursor()
    print("¡Conexión exitosa a PostgreSQL!")

    # 2. Creamos la tabla de usuarios profesionales (Cajón de archivos)
    # Usamos SERIAL para que el ID se sume solito (1, 2, 3...)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        correo VARCHAR(100)
    );
    """)
    conexion.commit()
    print("Tabla 'usuarios' lista en la base de datos.")

    # 3. Insertamos un usuario de prueba
    cursor.execute("""
    INSERT INTO usuarios (nombre, correo) 
    VALUES ('Desarrollador Profesional Linux', 'pro@correo.com');
    """)
    conexion.commit()
    print("Usuario guardado permanentemente en Postgres.")

    # 4. Leemos los datos para comprobar que sí se guardaron
    cursor.execute("SELECT * FROM usuarios;")
    todos = cursor.fetchall()

    print("\n--- REGISTROS EN POSTGRESQL ---")
    for u in todos:
        print(f"ID: {u[0]} | Nombre: {u[1]} | Correo: {u[2]}")

    # Cerramos las conexiones por seguridad
    cursor.close()
    conexion.close()
    print("\n Conexión cerrada de forma segura.")

except Exception as error:
    print("Hubo un error al conectar:", error)
