import tkinter as tk
from tkinter import messagebox
import math

class TrapecioIsosceles:
    def __init__(self, base_mayor: float, base_menor: float, altura: float):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Todas las dimensiones deben ser positivas.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self) -> float:
        lado = math.sqrt(((self.base_mayor - self.base_menor) / 2) ** 2 + self.altura ** 2)
        return self.base_mayor + self.base_menor + 2 * lado

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def obtener_nombre(self) -> str:
        return "Trapecio Isósceles"

def calcular():
    try:
        base_mayor = float(entry_base_mayor.get())
        base_menor = float(entry_base_menor.get())
        altura = float(entry_altura.get())
        trapecio = TrapecioIsosceles(base_mayor, base_menor, altura)
        resultado.config(
            text=f"{trapecio.obtener_nombre()}\nÁrea: {trapecio.calcular_area():.2f}\nPerímetro: {trapecio.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Trapecio Isósceles")
ventana.geometry("450x350")

tk.Label(ventana, text="Base Mayor:", font=("Arial", 14)).pack(pady=5)
entry_base_mayor = tk.Entry(ventana, font=("Arial", 14))
entry_base_mayor.pack()

tk.Label(ventana, text="Base Menor:", font=("Arial", 14)).pack(pady=5)
entry_base_menor = tk.Entry(ventana, font=("Arial", 14))
entry_base_menor.pack()

tk.Label(ventana, text="Altura:", font=("Arial", 14)).pack(pady=5)
entry_altura = tk.Entry(ventana, font=("Arial", 14))
entry_altura.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

