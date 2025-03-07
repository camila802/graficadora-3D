import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar_3d():
    try:
        expresion = entrada.get()
        if not expresion:
            messagebox.showerror("Error", "Debe ingresar una función")
            return
        
        print(f"Expresión ingresada: {repr(expresion)}")  # Depuración
        expresion = expresion.replace("^", "**")
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        
        print(f"Valores de X: {X[:2, :2]}")  # Depuración
        print(f"Valores de Y: {Y[:2, :2]}")  # Depuración
        
        funciones_permitidas = {"x": X, "y": Y, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                                "sqrt": np.sqrt, "log": np.log, "exp": np.exp, "abs": np.abs,
                                "pi": np.pi, "e": np.e}
        
        Z = eval(expresion, {"__builtins__": None}, funciones_permitidas)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title(f"Gráfica de Z = {expresion}")
        plt.show()
    
    except Exception as e:
        messagebox.showerror("Error", f"Expresión no válida: {e}")

root = tk.Tk()
root.title("Graficadora 3D")
root.geometry("400x200")

entrada = tk.Entry(root, width=30)
entrada.pack(pady=20)

boton = tk.Button(root, text="Graficar", command=graficar_3d)
boton.pack()

root.mainloop()
