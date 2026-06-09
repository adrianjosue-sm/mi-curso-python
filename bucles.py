import time  # Esto es un truco para que la computadora espere un segundo

print("🚀 --- EJEMPLO 1: LANZAMIENTO DEL COHETE (Bucle FOR) ---")

for segundo in range(5, 0, -1):
    print("Faltan", segundo, "segundos...")
    time.sleep(1)  # La computadora espera 1 segundo completo
    
print("💥 ¡¡¡DESPEGUEEEEE!!! 🚀\n")

print("🔐 --- EJEMPLO 2: EL GUARDIÁN DE LA PUERTA (Bucle WHILE) ---")
clave_correcta = "python123"
intento = ""

# MIENTRAS el intento sea diferente (!=) a la clave correcta, se repite el juego
while intento != clave_correcta:
    intento = input("Introduce la clave secreta para entrar: ")
    if intento != clave_correcta:
        print("\n ❌ Contraseña incorrecta. ¡Sigue intentando!")

print("🔓 ¡Acceso concedido! Bienvenido al sistema secreto.")
 