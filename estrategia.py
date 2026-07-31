# VARIABLE GLOBAL
compuesto_neumaticos = "Blandos"

def cambiar_estrategia():
    # VARIABLE LOCAL (Tiene el mismo nombre que la global)
    compuesto_neumaticos = "Duros"
    return compuesto_neumaticos


# --- EJECUCIÓN ---
compuesto_neumaticos=cambiar_estrategia()
print(f"1. Dentro de boxes los mecánicos montan: {compuesto_neumaticos}")
print(f"2. En la pista el auto está corriendo con: {compuesto_neumaticos}")