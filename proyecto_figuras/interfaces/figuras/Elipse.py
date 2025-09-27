import tkinter as tk
from tkinter import messagebox
import math


class Elipse:
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Los ejes deben ser valores positivos.")
        self.a = a
        self.b = b

    def calcular_perimetro(self) -> float:
        h = ((self.a - self.b) ** 2) / ((self.a + self.b) ** 2)
        return math.pi * (self.a + self.b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def calcular_area(self) -> float:
        return math.pi * self.a * self.b

    def obtener_nombre(self) -> str:
        return "Elipse"


def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        elipse = Elipse(a, b)
        resultado.config(
            text=f"{elipse.obtener_nombre()}\nÁrea: {elipse.calcular_area():.2f}\nPerímetro (aprox): {elipse.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Calculadora de Elipse")
ventana.geometry("700x300")


tk.Label(ventana, text="Eje mayor (a):", font=("Arial", 14)).pack(pady=5)
entry_a = tk.Entry(ventana, font=("Arial", 14))
entry_a.pack()

tk.Label(ventana, text="Eje menor (b):", font=("Arial", 14)).pack(pady=5)
entry_b = tk.Entry(ventana, font=("Arial", 14))
entry_b.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()
