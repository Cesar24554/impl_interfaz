import tkinter as tk
from tkinter import messagebox

class Rectangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    def calcular_area(self) -> float:
        return self.base * self.altura

    def obtener_nombre(self) -> str:
        return "Rectángulo"

def calcular():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        rectangulo = Rectangulo(base, altura)
        resultado.config(
            text=f"{rectangulo.obtener_nombre()}\nÁrea: {rectangulo.calcular_area():.2f}\nPerímetro: {rectangulo.calcular_perimetro():.2f}"
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Calculadora de Rectángulo")
ventana.geometry("450x300")

tk.Label(ventana, text="Base:", font=("Arial", 14)).pack(pady=5)
entry_base = tk.Entry(ventana, font=("Arial", 14))
entry_base.pack()

tk.Label(ventana, text="Altura:", font=("Arial", 14)).pack(pady=5)
entry_altura = tk.Entry(ventana, font=("Arial", 14))
entry_altura.pack()

tk.Button(ventana, text="Calcular", command=calcular, font=("Arial", 12)).pack(pady=15)

resultado = tk.Label(ventana, font=("Arial", 14))
resultado.pack(pady=20)

ventana.mainloop()

