# 1. DEFINE TU FUNCIÓN AQUÍ
def calcular_vuelta_rapida(tiempo_clasificacion, penalizacion):
    # Escribe tu lógica aquí adentro...
    # Recuerda usar 'return' para enviar el resultado hacia afuera
    tiempo_final = tiempo_clasificacion + penalizacion
    return tiempo_final
# 2. PROGRAMA PRINCIPAL (Mundo exterior)

# EXPERIMENTO DE SCOPE: 
# Si intentas descomentar la línea de abajo y ejecutar, Python va a explotar.
    print(tiempo_final) 


# SOLUCIÓN CORRECTA:
# Llama a tu función pasándole datos (Ej: 82.4 segundos de vuelta + 2.0 de penalización por límites de pista)
# Guarda el retorno en la variable 'record_oficial'

record_oficial = calcular_vuelta_rapida(82.4, 2.0)
# Imprime aquí abajo tu 'record_oficial' para verificar que todo sirva
print(record_oficial)