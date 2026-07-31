def limpiar_nombre_piloto(nombre_sucio):
    # 1. Quita espacios (.strip()) y pon mayúsculas iniciales (.title())
    # 2. DEVUELVE el resultado con return
    nombre_sucio=nombre_sucio.strip().title()
    return nombre_sucio

    

def calcular_combustible(vueltas, consumo_vuelta, seguridad):
    # 1. Multiplica vueltas por consumo y súmale la seguridad
    # 2. DEVUELVE el resultado con return
    total_litros=(vueltas*consumo_vuelta) + seguridad
    return total_litros


# --- PRUEBA DEL SCRIPT ---
if __name__ == "__main__":
    piloto = "   cHaRlEs lEcLeRc   "
    piloto_limpio = limpiar_nombre_piloto(piloto)

    # 25 vueltas, 2.1 litros por vuelta, 4 litros de reserva
    combustible_total = calcular_combustible(25, 2.1, 4)
    
    print("=== TELEMETRÍA INICIAL ===")
    print(f"Piloto Confirmado: {piloto_limpio}")
    print(f"Carga de Combustible Necesaria: {combustible_total} Litros")