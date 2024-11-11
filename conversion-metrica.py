"""
# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms
    Mostrar mensaje: "Por favor, ingresar las medidas de la pieza del mueble (en cms): "

    # Paso 2: Convertir las medidas de centímetros a pulgadas
    Convertir medidas_en_pulgadas = medidas_en_cms / 2.54

    # Paso 3: Mostrar las medidas en pulgadas al usuario
    Mostrar mensaje: "Las medidas en pulgadas de la pieza ingresada son:", medidas_en_pulgadas
"""
# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medidas_en_cms = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de centímetros a pulgadas

medidas_en_pulgadas = medidas_en_cms / 2.54

# Paso 3: Mostrar las medidas en pulgadas al usuario

print(f"Las medidas en pulgadas de la pieza ingresada son: {medidas_en_pulgadas}")