import pandas as pd

# Diccionario de datos
datos = {
    'Estudiante': ['Rosa', 'David', 'Elena', 'Mario', 'Paula'],
    'Dias_prestamo': [7, 10, 5, 12, 3]
}

# Convertir el diccionario a un DataFrame
df = pd.DataFrame(datos)

# Estadísticas descriptivas de los días de préstamo
stats = df['Dias_prestamo'].describe()

# Calcular promedio y máximo de días de préstamo
dias_promedio = stats['mean']
max_dias = stats['max']

# Filtrar los estudiantes que retuvieron el libro más de 8 días
df_mayor_8 = df[df['Dias_prestamo'] > 8]
lista_altos = df_mayor_8['Estudiante'].tolist()

# RESULTADOS
print("==== RESULTADOS ==== ")
print(f"\nLa cantidad promedio de días que prestaron un libro fue: {int(dias_promedio)} días.")
print(f"\nLa cantidad máxima de días que prestaron un libro fue: {int(max_dias)} días.")

# Mostrar estudiantes que retuvieron el libro por más de 8 días
print(f"\nLos estudiantes que retuvieron un libro por más de 8 días fueron:")
for alumno in lista_altos:
    print(f"-> {alumno}")
