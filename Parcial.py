def parcial():
    temperaturas = [21, 23, 26, 22, 29, 30, 33, 32, 31, 30, 29, 27, 32, 36, 35,
                    30, 31, 27, 23, 20, 18, 17, 19, 28, 34, 31, 38, 39, 35, 33]
    temp_max = 0
    temp_min = 40
    temp_aux = 0
    promedio = 30
    temp_anunciada = 0
    for temperatura in temperaturas:
        if temperatura > temp_max:
            temp_max = temperatura
        if temperatura < temp_min:
            temp_min = temperatura
        if temperatura > 25:
            temp_anunciada += 1
        temp_aux += temperatura
    temp_aux = temp_aux / promedio
    print(f"El dia mas caluroso es: {temp_max}")
    print(f"El dia mas frio es: {temp_min}")
    print(f"Los dias que superaron los 25°C son: {temp_anunciada} dias")
    print(f"El promedio de las temperaturas del mes es: {temp_aux}")
parcial()
