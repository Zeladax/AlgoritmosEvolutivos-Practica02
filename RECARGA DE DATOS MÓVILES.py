import numpy as np
 
# Definimos los tamaños de los paquetes (en GB)
paquetes = np.array([1, 2, 5, 10])

# Definimos los precios de los paquetes (en S/)
precios = np.array([5, 9, 20, 35])

# Calcular el costo por GB para cada paquete
costo_GB = precios / paquetes

# Encontrar el costo más económico
costo_min = costo_GB.min()
indice_min = costo_GB.argmin()

# Mostrar los resultados
print("=== Costo por GB de cada paquete ===")
for i, paquete in enumerate(paquetes):
    print(f"En el paquete de {paquetes[i]}GB, el costo por GB es de S/{costo_GB[i]:.2f}")

print(f"\nEl paquete de {paquetes[indice_min]}GB es el más económico con un costo de S/{costo_min:.2f} por GB.")
