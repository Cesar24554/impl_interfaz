import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def obtener_nombre(self):
        return "Círculo"

class Cuadrado:
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 4 * self.lado

    def calcular_area(self):
        return self.lado ** 2

    def obtener_nombre(self):
        return "Cuadrado"

class Elipse:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Los ejes deben ser valores positivos.")
        self.a = a
        self.b = b

    def calcular_perimetro(self):
        h = ((self.a - self.b)**2) / ((self.a + self.b)**2)
        return math.pi * (self.a + self.b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def calcular_area(self):
        return math.pi * self.a * self.b

    def obtener_nombre(self):
        return "Elipse"

class Hexagono:
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 6 * self.lado

    def calcular_area(self):
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)

    def obtener_nombre(self):
        return "Hexágono Regular"

class Rectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def calcular_area(self):
        return self.base * self.altura

    def obtener_nombre(self):
        return "Rectángulo"

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        if diagonal_mayor <= 0 or diagonal_menor <= 0:
            raise ValueError("Las diagonales deben ser valores positivos.")
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_perimetro(self):
        lado = math.sqrt((self.diagonal_mayor / 2) ** 2 + (self.diagonal_menor / 2) ** 2)
        return 4 * lado

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def obtener_nombre(self):
        return "Rombo"

class Semicirculo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo.")
        self.radio = radio

    def calcular_perimetro(self):
        return math.pi * self.radio + 2 * self.radio

    def calcular_area(self):
        return (math.pi * self.radio ** 2) / 2

    def obtener_nombre(self):
        return "Semicírculo"

class TrapecioIsosceles:
    def __init__(self, base_mayor, base_menor, altura):
        if base_mayor <= 0 or base_menor <= 0 or altura <= 0:
            raise ValueError("Todas las dimensiones deben ser positivas.")
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def calcular_perimetro(self):
        lado = math.sqrt(((self.base_mayor - self.base_menor) / 2) ** 2 + self.altura ** 2)
        return self.base_mayor + self.base_menor + 2 * lado

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def obtener_nombre(self):
        return "Trapecio Isósceles"

class TrianguloEquilatero:
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser un valor positivo.")
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_area(self):
        return (math.sqrt(3) / 4) * (self.lado ** 2)

    def obtener_nombre(self):
        return "Triángulo Equilátero"

class TrianguloRectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser valores positivos.")
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        return self.base + self.altura + hipotenusa

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def obtener_nombre(self):
        return "Triángulo Rectángulo"

# Definición de campos requeridos para cada figura
figuras = {
    "Círculo": {"clase": Circulo, "campos": ["radio"]},
    "Cuadrado": {"clase": Cuadrado, "campos": ["lado"]},
    "Elipse": {"clase": Elipse, "campos": ["a", "b"]},
    "Hexágono Regular": {"clase": Hexagono, "campos": ["lado"]},
    "Rectángulo": {"clase": Rectangulo, "campos": ["base", "altura"]},
    "Rombo": {"clase": Rombo, "campos": ["diagonal_mayor", "diagonal_menor"]},
    "Semicírculo": {"clase": Semicirculo, "campos": ["radio"]},
    "Trapecio Isósceles": {"clase": TrapecioIsosceles, "campos": ["base_mayor", "base_menor", "altura"]},
    "Triángulo Equilátero": {"clase": TrianguloEquilatero, "campos": ["lado"]},
    "Triángulo Rectángulo": {"clase": TrianguloRectangulo, "campos": ["base", "altura"]},
}

def actualizar_campos(*args):
    figura = opcion_figura.get()
    for widget in frame_campos.winfo_children():
        widget.destroy()
    campos = figuras[figura]["campos"]
    entries.clear()
    for campo in campos:
        lbl = tk.Label(frame_campos, text=f"{campo.replace('_', ' ').capitalize()}:", font=("Arial", 12))
        lbl.pack(anchor="w", pady=2)
        ent = tk.Entry(frame_campos, font=("Arial", 12))
        ent.pack(fill="x", pady=2)
        entries[campo] = ent
    resultado.config(text="")

def calcular():
    figura = opcion_figura.get()
    clase = figuras[figura]["clase"]
    try:
        # Verificar campos vacíos
        for campo in figuras[figura]["campos"]:
            if entries[campo].get().strip() == "":
                messagebox.showerror("Error", f"Por favor, ingresa el valor para {campo.replace('_', ' ')}.")
                return

        valores = {campo: float(entries[campo].get()) for campo in figuras[figura]["campos"]}
        instancia = clase(**valores)
        area = instancia.calcular_area()
        perimetro = instancia.calcular_perimetro()
        resultado.config(text=f"{instancia.obtener_nombre()}\n\nÁrea: {area:.2f}\nPerímetro: {perimetro:.2f}", fg="blue")
    except ValueError as ve:
        messagebox.showerror("Error de valor", str(ve))
    except Exception:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def limpiar():
    for entry in entries.values():
        entry.delete(0, tk.END)
    resultado.config(text="")

ventana = tk.Tk()
ventana.title("Calculadora de Figuras Geométricas")
ventana.geometry("450x500")
ventana.resizable(False, False)

tk.Label(ventana, text="Selecciona una figura:", font=("Arial", 14)).pack(pady=10)

opcion_figura = tk.StringVar()
opcion_figura.set("Círculo")
opcion_figura.trace_add("write", actualizar_campos)

menu_figuras = tk.OptionMenu(ventana, opcion_figura, *figuras.keys())
menu_figuras.config(font=("Arial", 12))
menu_figuras.pack()

frame_campos = tk.Frame(ventana)
frame_campos.pack(pady=15, fill="x", padx=20)

entries = {}

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_calcular = tk.Button(frame_botones, text="Calcular", command=calcular, font=("Arial", 14), width=10)
boton_calcular.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar, font=("Arial", 14), width=10)
boton_limpiar.grid(row=0, column=1, padx=10)

resultado = tk.Label(ventana, font=("Arial", 14), justify="center")
resultado.pack(pady=20)

actualizar_campos()

ventana.mainloop()

