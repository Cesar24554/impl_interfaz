import tkinter as tk
from tkinter import messagebox
import math

class Rombo:
    def __init__(self, diagonal_mayor: float, diagonal_menor: float):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser valores positivos.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self) -> float:
        lado = math.sqrt((self.diagonal_mayor / 2) ** 2 + (self.diagonal_menor / 2) ** 2)
        return 4 * lado

    def calcular_area(self) -> float:
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self) -> str:
        return "Rombo"

def calcular():
    try:
        d_mayor = float(entry_diag_mayor.get())
        d_menor = float(entry_diag_menor.get())
        rombo = Rombo(d_mayor, d_menor)
        resultado.config(
            text=f"{rombo.obtener_nombre()}\nÁrea: {rombo.calcular_area():.2f}\nPerímetro: {rombo.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Rombo")
ventana.geometry("450x300")

tk.Label(ventana, text="Diagonal Mayor:", font=("Arial", 14)).pack(pady=5)
entry_diag_mayor = tk.Entry(ventana, font=("Arial", 14))
entry_diag_mayor.pack()

tk.Label(ventana, text="Diagonal Menor:", font=("Arial", 14)).pack(pady=5)
entry_diag_menor = tk.Entry(ventana, font=("Arial", 14))
entry_diag_menor.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

