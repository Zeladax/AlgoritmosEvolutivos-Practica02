import numpy as np

# Definimos el presupuesto de Carla
presupuesto = 15.0

# Definimos los precios de transporte (Bus, Combi, Tren)
precios = np.array([2.50, 3.0, 1.80])

# Calculamos cuántos viajes puede realizar con el presupuesto en cada medio de transporte
# np.floor redondea hacia abajo al número entero más cercano
max_viajes = np.floor(presupuesto / precios)

# Encontramos el medio de transporte que permite la mayor cantidad de viajes
cantidad_max = int(max_viajes.max())
indice_max = int(max_viajes.argmax())

# Nombres de los medios de transporte
movilidades = ['Bus', 'Combi', 'Tren']

# RESULTADOS DE VIAJES
print("======== RESULTADOS DE VIAJES ========")

# Mostramos los viajes posibles en cada medio de transporte
for i, movilidad in enumerate(movilidades):
    print(f"El viaje en {movilidad} cuesta: S/{precios[i]:.2f} y se pueden realizar {int(max_viajes[i])} viajes")

# Mostramos el medio de transporte con la mayor cantidad de viajes
print(f"\nEl viaje en {movilidades[indice_max]} le permite realizar la mayor cantidad de viajes ({cantidad_max} viajes) con un presupuesto de S/{presupuesto:.2f}.")
