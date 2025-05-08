import numpy as np

# Presupuesto de Maria
presupuesto = 8.0
 
# Precios de las copisterías
precios = np.array([0.10, 0.12, 0.08])

# Calcular cuántas páginas puede fotocopiar en cada copistería
# np.floor se usa para obtener el número entero hacia abajo
max_copias = np.floor(presupuesto / precios)

# Obtener la cantidad máxima de páginas y la copistería que la ofrece
cantidad_max = int(max_copias.max())
indice_max = int(max_copias.argmax())

# Nombres de las copisterías
nombres = ['A', 'B', 'C']

# RESULTADOS
print("========== Resultados Copisterías ==========")
for i, nombre in enumerate(nombres):
    print(f"Copistería {nombre}: precio S/{precios[i]:.2f} → se pueden sacar {int(max_copias[i])} páginas")

# Copistería que ofrece la mayor cantidad de páginas
print(f"\nCon un presupuesto de S/{presupuesto}, la copistería que ofrece más páginas es la Copistería {nombres[indice_max]} con {cantidad_max} páginas.")
