# 1. Creamos el MOLDE (La Clase)
class Heroe:
    # Este es el constructor, define qué características tiene cada héroe al nacer
    def __init__(self, nombre, puntos_vida):
        self.nombre = nombre  #Atributo 1
        self.vida = puntos_vida  #Atributo 2
        
    # Esta es una acción que el héroe sabe hacer (Un Método)
    def atacar(self, enemigo):
        print(f"{self.nombre} ataca {enemigo} ! Golpe critico.")
    
# 2. ¡Vamos a sacar galletas del horno! (Crear Objetos reales)
personaje_1 = Heroe("Guerrero Linux", 100)
personaje_2 = Heroe("Mago python", 80)

# 3. Usamos los objetos y sus superpoderes
print("---NUESTROS HEROES---")
print(f"Heroe 1: {personaje_1.nombre} tiene {personaje_1.vida} de vida.")
print(f"Heroe 2: {personaje_2.nombre} tiene {personaje_2.vida} de vida. \n")

# Hacemos que hagan acciones
personaje_1.atacar("UN MOUSTRO DE BUGS")
personaje_2.atacar("UN DRAGON DE ERRORES DE CODIGO")

#Crear un tercer héroe llamado "Arquero Terminal" con 90 puntos de vida usando nuestro molde.
personaje_3 = Heroe("Arquero Terminal", 90)
print("***NACE UN NUEVO HEROE***")
print(f"Heroe 3: {personaje_3.nombre} tiene {personaje_3.vida} de vida. \n")
personaje_3.atacar("UNA BRUJA MALVADA")

