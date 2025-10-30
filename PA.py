import math

# ======================================================================
# FUNCIONES MATEMÁTICAS BÁSICAS
# ======================================================================

def producto_cruz(v1, v2):
    """Calcula el producto vectorial (cruz) entre dos vectores 3D."""
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return [x, y, z]

def producto_punto(v1, v2):
    """Calcula el producto escalar (punto) entre dos vectores 3D."""
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def restar_puntos(p_final, p_inicial):
    """Calcula el vector restando las coordenadas de dos puntos: P_final - P_inicial."""
    return [p_final[i] - p_inicial[i] for i in range(3)]

# ======================================================================
# FUNCIÓN PRINCIPAL DE CÁLCULO DE VOLUMEN
# ======================================================================

def volumen_paralelepipedo(a, b, c):
    """
    Calcula el volumen del paralelepípedo definido por tres vectores (a, b, c) 
    utilizando el valor absoluto del triple producto escalar.
    """
    if len(a) != 3 or len(b) != 3 or len(c) != 3:
        raise ValueError("Todos los vectores deben ser de 3 componentes.")
    
    # Triple Producto Escalar: a . (b x c)
    producto_vec = producto_cruz(b, c)
    triple_producto = producto_punto(a, producto_vec)
    volumen = abs(triple_producto)
    
    return volumen

# ======================================================================
# FUNCIÓN DE ENTRADA DE DATOS ROBUSTA (Permite al usuario ingresar los datos)
# ======================================================================

def obtener_punto(nombre):
    """Solicita al usuario las 3 coordenadas de un punto."""
    while True:
        try:
            entrada = input(f"Introduce las 3 coordenadas del punto {nombre} (ej: 1,2,3): ")
            
            # Limpiar espacios, dividir por comas y filtrar elementos vacíos
            componentes_str = [comp.strip() for comp in entrada.split(',')]
            componentes_str = [comp for comp in componentes_str if comp]
            
            # Convertir a flotante (debe usarse punto '.' para decimales)
            componentes = [float(comp) for comp in componentes_str]
            
            if len(componentes) != 3:
                print(f"Error: Debes introducir exactamente 3 números. Se encontraron {len(componentes_str)} elementos.")
                continue
            return componentes
        
        except ValueError:
            print("Error: Asegúrate de que todos los valores sean números válidos (usa el punto '.' como separador decimal).")

# ======================================================================
# EJECUCIÓN PRINCIPAL (Modo Calculadora)
# ======================================================================

if __name__ == "__main__":
    print("\n--- Calculadora de Volumen de Paralelepípedo ---")
    print("Por favor, ingresa las coordenadas de los 4 vértices adyacentes al origen.")
    
    try:
        # 1. Solicitar los 4 puntos al usuario
        P_A = obtener_punto("A (Origen)")
        P_B = obtener_punto("B (Vértice 1)")
        P_C = obtener_punto("C (Vértice 2)")
        P_D = obtener_punto("D (Vértice 3)")
        
        # 2. Convertir puntos a vectores (a = B-A, b = C-A, c = D-A)
        a = restar_puntos(P_B, P_A)
        b = restar_puntos(P_C, P_A)
        c = restar_puntos(P_D, P_A)
        
        # 3. Calcular el volumen
        volumen = volumen_paralelepipedo(a, b, c)
        
        # 4. Mostrar el resultado en el formato solicitado
        print("\n--- Resultados ---")
        print(f"Puntos: A={P_A}, B={P_B}, C={P_C}, D={P_D}")
        
        print("\nVectores de las aristas:")
        print(f"a = B - A = {a}")
        print(f"b = C - A = {b}")
        print(f"c = D - A = {c}")

        print(f"\nEl volumen del paralelepípedo es: {volumen:.4f} unidades cúbicas.")

    except Exception as e:
        print(f"\nOcurrió un error: {e}")