# Le preguntamos al usuario su estatura (y la convertimos a un número entero)
estatura = int(input("Hola, ¿Cuanto mides en centimetros? "))

# Aquí viene el policía de tránsito a tomar decisiones
if estatura >= 150:
    print("✅ ¡Bienvenido! Eres lo suficientemente alto para subir a la Montaña Rusa. ¡Disfruta el viaje!")
elif estatura >= 120:
    print("⚠️ Puedes subir, pero SOLO si te acompaña un adulto responsable.")
else:
    print("❌ Lo siento mucho, pequeñín. Por seguridad, no puedes subir todavía. ¡Intenta en el carrusel!")

print("Gracias por visitar el parque.")