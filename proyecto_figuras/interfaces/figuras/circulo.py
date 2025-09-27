# figuras/circulo.py
import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser positivo.")
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def obtener_nombre(self):
        return "Círculo"

def calcular():
    try:
        r = float(entrada.get())
        c = Circulo(r)
        resultado.config(
            text=f"{c.obtener_nombre()}\nÁrea: {c.calcular_area():.2f}\nPerímetro: {c.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))


ventana = tk.Tk()
ventana.title("Calculadora de Círculo")
ventana.geometry("700x300") 

tk.Label(ventana, text="Ingresa el radio:", font=("Arial", 14)).pack(pady=15)

entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()
