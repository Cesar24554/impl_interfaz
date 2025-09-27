import tkinter as tk
from tkinter import messagebox
import math

class Semicirculo:
    def __init__(self, radio: float):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self) -> float:
        return math.pi * self.radio + 2 * self.radio  # arco + diámetro

    def calcular_area(self) -> float:
        return (math.pi * self.radio ** 2) / 2

    def obtener_nombre(self) -> str:
        return "Semicírculo"

def calcular():
    try:
        radio = float(entry.get())
        semi = Semicirculo(radio)
        resultado.config(
            text=f"{semi.obtener_nombre()}\nÁrea: {semi.calcular_area():.2f}\nPerímetro: {semi.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Semicírculo")
ventana.geometry("400x300")

tk.Label(ventana, text="Ingresa el radio:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(ventana, font=("Arial", 14))
entry.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()
