# 1. Definimos la función
def calcular_consumo(vueltas, consumo_por_vuelta):
    total = vueltas * consumo_por_vuelta
    return total  # <-- Devuelve el resultado al programa principal

# 2. La usamos (la llamamos)
combustible_necesario = calcular_consumo(15, 3.2)   
print(f"Necesitas {combustible_necesario} litros.")