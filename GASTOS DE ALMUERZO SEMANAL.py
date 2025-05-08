import pandas as pd

# Definimos el diccionario de datos
datos = {
    'Gasto': [4.0, 3.5, 5.0, 4.2, 3.8],
    'Dias': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
}

# Definimos el DataFrame
df = pd.DataFrame(datos)

# Calcular el gasto total de la semana
df_gastoTotal = df['Gasto'].sum()

# Calcular el gasto promedio de la semana
df_gastoPromedio = df['Gasto'].mean()

# Identificar los días en los que el gasto fue mayor que el promedio
df_mayorPromedio = df[df['Gasto'] > df_gastoPromedio]
listaMayores = df_mayorPromedio['Dias'].tolist()

# Mostrar resultados
print(f"El gasto total de la semana fue: S/{df_gastoTotal:.2f}")
print(f"\nEl gasto promedio de la semana fue: S/{df_gastoPromedio:.2f}")

# Mostrar los días en los que el gasto fue mayor que el promedio
print(f"\nLos días en los que el gasto fue mayor que el promedio son:")
for i in listaMayores:
    print(f"-> {i}")
