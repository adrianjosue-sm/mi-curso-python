"""
Vamos a construir una máquina que 
reciba el precio de un producto y nos 
devuelva el precio total con el impuesto incluido.
"""

# 1. Aquí construimos la máquina llamada 'calcular_total'
# Recibe un 'precio_base' (materia prima)
def calcular_total(precio_base):
    impuestos = precio_base * 0.16  # En Mexico el IVA es del 16%  
    precio_final = precio_base + impuestos  
    return precio_final  # Regresa el producto terminado

# 2. ¡Vamos a usar la máquina! (Llamar a la función)
# Metemos una playera de 100 pesos a la máquina
total_playera = calcular_total(100)
print("El costo total de la playera incluyendo impuestos es de: $", total_playera)

# Metemos unos tenis de 500 pesos a la misma máquina
costo_tenis = 500
costo_total_tenis = calcular_total(costo_tenis)
print("El costo total de los tenis incluyendo impuestos es de: $", costo_total_tenis)

# Ahora solicitaremos que el usuario ingrese los datos del producto
precio_usuario = float(input("\nIntroduce el prcio del producto: $"))
precio_total_usuario = calcular_total(precio_usuario)
print("El costo total de este producto incluyendo impuestos es de: $", precio_total_usuario)




    