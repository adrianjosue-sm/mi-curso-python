# CON ESTOS EJERCICIOS APRENDEREMOS UN POCO SOBRE LAS LISTAS Y LOS DICCIONARIOS
# Vamos a crear un sistema que maneje una lista de juegos más vendidos y un diccionario con los detalles de una consola.

print("---EJEMPLO 1: NUESTRA LISTA DE VIDEOJUEGOS---")

# Creamos una lista usando corchetes [ ]
juegos = ["Minecraft", "Zelda", "Mario Kart"]

# Ver la lista completa
print("Lista completa de videojuegos: ", juegos)

# Ver solo el primer videojuego.
print("El juego en la posicion 1 es: ", juegos[0])

# Agregamos un videojuego mas al final de la lista.
juegos.append("Sonic")
print("Lista actualizada: ", juegos)


print("\n ---EJEMPLO 2: EL DICCIONARIO DE LA CONSOLA---")

# Creamos un diccionario usando llaves { }
consola = {
    "nombre": "Play Station",
    "color": "Negro y plateado",
    "almacenamiento_GB": 64,
    "nueva": True
}

# Ver tola la informacion de la consola.
print("Ficha tecnica de la consola:", consola)

# Buscar un dato específico usando su clave entre corchetes
print("¿De qué color es?: ", consola["color"])
print("¿Cuánta memoria tiene?: ", consola["almacenamiento_GB"], "GB")