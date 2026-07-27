vida_maxima = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))

porcentaje = (vida_actual / vida_maxima) * 100

print("Vida restante:", porcentaje, "%")