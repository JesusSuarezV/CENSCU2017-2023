import tkinter as tk
import costo_unitario as cu


def cu2017():
    print("xd")
    cu.importarCSV("2017")


def cu2018():
    cu.importarCSV("2018")


def cu2019():
    cu.importarCSV("2019")


def cu2020():
    cu.importarCSV("2020")


def cu2021():
    cu.importarCSV("2021")


def cu2022():
    cu.importarCSV("2022")


def cu2023():
    cu.importarCSV("2023")


ventana = tk.Tk()

ventana.title("TARIFA DE ENERGIA POR KWH DE LA CIUDAD DE CÚCUTUA")
ventana.geometry("800x700")
titulo_fuente = ("HELVETICA", 20)

titulo = tk.Label(
    ventana, text="TARIFA DE ENERGIA DE LA CIUDAD DE CÚCUTUA", font=("HELVETICA", 20))
titulo.pack(padx=20, pady=20)

subtitulo = tk.Label(
    ventana, text="Por favor, seleccione el año a consultar", font=("HELVETICA", 10))
subtitulo.pack(padx=10, pady=10)

boton = tk.Button(
    ventana, text="2017", command=cu2017, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2018", command=cu2018, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2019", command=cu2019, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2020", command=cu2020, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2021", command=cu2021, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2022", command=cu2022, width=70, height=2)
boton.pack(pady=20)

boton = tk.Button(
    ventana, text="2023", command=cu2023, width=70, height=2)
boton.pack(pady=20)

ventana.mainloop()
