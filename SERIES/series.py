import pandas as pd

# ===== PUNTO 1: Crear las Series =====

# Índice: Región, Valores: Porcentaje de energía renovable 
energia_renovable = pd.Series([85, 78, 65, 92, 55], 
    index=['América Latina', 'Europa', 'Asia', 'África', 'América del Norte']) 

# Índice: Ciudad, Valores: Residuos per cápita (kg/día) 
residuos_pc = pd.Series([1.2, 1.5, 0.8, 2.1, 1.1], 
    index=['Bogotá', 'Nueva York', 'Tokio', 'Dubái', 'París']) 

# Índice: País, Valores: Emisiones de CO2 per cápita (toneladas) 
emisiones_co2 = pd.Series([4.5, 16.2, 7.8, 1.9, 12.5], 
    index=['Brasil', 'Estados Unidos', 'Alemania', 'Nigeria', 'Canadá']) 

# Índice: Zona boscosa, Valores: Tasa de deforestación anual (%) 
deforestacion = pd.Series([0.5, 1.2, 0.8, 2.5, 0.3], 
    index=['Amazonía', 'Congo', 'Borneo', 'Siberia', 'Canadá'])


# ===== PUNTO 2: Estadísticas básicas =====

promedio_energia = energia_renovable.mean()
max_residuos = residuos_pc.max()
min_residuos = residuos_pc.min()
promedio_CO2 = emisiones_co2.mean()
desviacion_CO2 = emisiones_co2.std()
suma_deforestacion = deforestacion.sum()

print("===== PUNTO 2: Estadísticas =====")
print("Promedio energía renovable:", promedio_energia)
print("Máximo residuos por cápita:", max_residuos)
print("Mínimo residuos por cápita:", min_residuos)
print("Promedio emisiones CO2:", promedio_CO2)
print("Desviación estándar CO2:", desviacion_CO2)
print("Suma total tasa de deforestación:", suma_deforestacion)


# ===== PUNTO 3: Filtrados booleanos =====

# 3.1 Regiones con >80% energía renovable
regiones_mayor_80 = energia_renovable[energia_renovable > 80]

# 3.2 Ciudad con menor residuos per cápita
ciudad_menor_residuo = residuos_pc.idxmin()

# 3.3 Países con CO2 < 10 toneladas
paises_bajas_emisiones = emisiones_co2[emisiones_co2 < 10]

# 3.4 Zonas boscosas con deforestación > 1%
zonas_alta_deforestacion = deforestacion[deforestacion > 1]

print("===== PUNTO 3: Filtrados =====")
print(" Regiones con >80% energía renovable:")
print(regiones_mayor_80)
print(" Ciudad con menor residuos por cápita:", ciudad_menor_residuo)
print("Países con emisiones CO2 < 10 toneladas:")
print(paises_bajas_emisiones)
print("Zonas con deforestación > 1%:")
print(zonas_alta_deforestacion)


# ===== PUNTO 4: Ciudades con <1.5 kg/día residuos y país <10 ton CO2 =====

# Correspondencia ciudad → país
ciudad_a_pais = {
    'Bogotá': 'Brasil',
    'Tokio': 'Alemania',
    'París': 'Brasil'
}

ciudades_bajo_residuo = residuos_pc[residuos_pc < 1.5]
ciudades_filtradas = []

for ciudad in ciudades_bajo_residuo.index:
    if ciudad in ciudad_a_pais:
        pais = ciudad_a_pais[ciudad]
        if emisiones_co2[pais] < 10:
            ciudades_filtradas.append(ciudad)

print("==== PUNTO 4: Ciudades con residuos <1.5 kg/día y país con CO2 <10t =====")
print(ciudades_filtradas)


# ===== PUNTO 5: Región con <70% energía renovable y menor deforestación =====

# Correspondencia región → zona boscosa
region_a_bosque = {
    'Asia': 'Borneo',
    'América del Norte': 'Canadá'
}

# Filtrar regiones con <70% energía renovable
regiones_baja_renovable = energia_renovable[energia_renovable < 70]

# Evaluar tasa de deforestación de esas regiones
tasas = {}
for region in regiones_baja_renovable.index:
    if region in region_a_bosque:
        bosque = region_a_bosque[region]
        tasa = deforestacion[bosque]
        tasas[region] = tasa

region_menor_deforestacion = min(tasas, key=tasas.get)

print("===== PUNTO 5: Región con <70% energía renovable y menor deforestación =====")
print("Región seleccionada:", region_menor_deforestacion)



