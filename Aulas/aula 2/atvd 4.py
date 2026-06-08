temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for temp in temperaturas:
    if temp < 37.5:
        situacao = "Normal"
    elif temp <= 38.5:
        situacao = "Febre moderada"
    else:
        situacao = "Febre alta"

    print(f"{temp}°C → {situacao}")