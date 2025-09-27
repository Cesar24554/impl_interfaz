import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado

    def calcular_area(self) -> float:
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self) -> str:
        return "Triángulo Equilátero"

def calcular():
    try:
        lado = float(entry.get())
        triangulo = TrianguloEquilatero(lado)
        resultado.config(
            text=f"{triangulo.obtener_nombre()}\nÁrea: {triangulo.calcular_area():.2f}\nPerímetro: {triangulo.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Triángulo Equilátero")
ventana.geometry("400x300")

tk.Label(ventana, text="Ingresa el lado:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(ventana, font=("Arial", 14))
entry.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 3 * self.lado

    def calcular_area(self) -> float:
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self) -> str:
        return "Triángulo Equilátero"

def calcular():
    try:
        lado = float(entry.get())
        triangulo = TrianguloEquilatero(lado)
        resultado.config(
            text=f"{triangulo.obtener_nombre()}\nÁrea: {triangulo.calcular_area():.2f}\nPerímetro: {triangulo.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Triángulo Equilátero")
ventana.geometry("400x300")

tk.Label(ventana, text="Ingresa el lado:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(ventana, font=("Arial", 14))
entry.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

