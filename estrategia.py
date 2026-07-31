# VARIABLE GLOBAL
compuesto_neumaticos = "Blandos"

def cambiar_estrategia():
    # VARIABLE LOCAL (Tiene el mismo nombre que la global)
    compuesto_neumaticos = "Duros"
    print(f"1. Dentro de boxes los mecánicos montan: {compuesto_neumaticos}")

# --- EJECUCIÓN ---
cambiar_estrategia()
print(f"2. En la pista el auto está corriendo con: {compuesto_neumaticos}")