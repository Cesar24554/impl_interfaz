import tkinter as tk
from tkinter import messagebox


class Cuadrado:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

    def calcular_area(self) -> float:
        return self.lado ** 2

    def obtener_nombre(self) -> str:
        return "Cuadrado"


def calcular():
    try:
        lado = float(entry.get())
        cuadrado = Cuadrado(lado)
        resultado.config(
            text=f"{cuadrado.obtener_nombre()}\nÁrea: {cuadrado.calcular_area():.2f}\nPerímetro: {cuadrado.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Cuadrado")
ventana.geometry("700x300")  
# Widgets
tk.Label(ventana, text="Ingresa el lado:", font=("Arial", 14)).pack(pady=10)
entry = tk.Entry(ventana, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=10)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

