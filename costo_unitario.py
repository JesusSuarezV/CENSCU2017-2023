import pandas as pd
import matplotlib.pyplot as plt


def importarCSV(año):
    csv = pd.read_csv(f"CSV/{año}.csv", sep=',', decimal='.')
    dataframe = pd.DataFrame(csv[["Mes", "Costo Unitario"]])
    mes = dataframe.head(12)
    print(mes)
    promedio = round(mes["Costo Unitario"].mean(), 1)
    print(f"CU Promedio: {promedio}")

    x = csv["Mes"]
    y = csv["Costo Unitario"]

    plt.figure(figsize=(14, 10))
    plt.xlabel(
        f'Mes \n\n El Costo Unitario Promedio fue de {promedio}', fontsize=18)
    plt.ylabel('Costo Unitario (En Pesos por kWh)', fontsize=16)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.title(f"COSTO UNITARIO EN EL AÑO {año}")
    plt.gcf().canvas.manager.set_window_title(
        f"TARIFA DE ENERGIA EN EL AÑO {año}")
    plt.show()
