# VARIABLE GLOBAL (Visible en todo el circuito)
LIMITE_VELOCIDAD = 60 

def activar_limitador(velocidad_actual):
    # Intentemos cambiar el límite global desde aquí adentro a 80
    global LIMITE_VELOCIDAD
    LIMITE_VELOCIDAD = 80 
    
    if velocidad_actual > LIMITE_VELOCIDAD:
        return "¡MULTA! Exceso de velocidad en pits."
    else:
        return "Velocidad permitida."

# --- PRUEBA EN PISTA ---
print(activar_limitador(75))
print(f"El límite de velocidad global sigue siendo: {LIMITE_VELOCIDAD}")