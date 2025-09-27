import tkinter as tk
from tkinter import messagebox
import math


class Hexagono:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 6 * self.lado

    def calcular_area(self) -> float:
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)

    def obtener_nombre(self) -> str:
        return "Hexágono Regular"


def calcular():
    try:
        lado = float(entry.get())
        hexagono = Hexagono(lado)
        resultado.config(
            text=f"{hexagono.obtener_nombre()}\nÁrea: {hexagono.calcular_area():.2f}\nPerímetro: {hexagono.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Calculadora de Hexágono Regular")
ventana.geometry("700x300")


tk.Label(ventana, text="Ingresa el lado:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(ventana, font=("Arial", 14))
entry.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

