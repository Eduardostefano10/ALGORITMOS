import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk, filedialog

def cargar_analizar_mostrar():
    # Paso 1: Cargar datos desde un archivo Excel
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    if not ruta_archivo:
        return
    
    # Leer datos y realizar análisis
    df = pd.read_excel(ruta_archivo)
    
    # Paso 2: Preparar datos para el análisis
    # Seleccionar todas las variables del DataFrame
    variables = df.drop('Ingresos(Y)', axis=1)
    y = np.array(df['Ingresos(Y)'])

    # Paso 3: Realizar análisis
    modelo = LinearRegression()
    modelo.fit(variables, y)
    predicciones = modelo.predict(variables)
    coeficiente_pearson = np.corrcoef(predicciones, y)[0, 1]

    # Paso 4: Mostrar resultados en una interfaz gráfica
    root = tk.Tk()
    root.title("Análisis de Regresión Lineal")

    style = ttk.Style()
    style.configure('TFrame', background='#333')
    style.configure('TButton', background='#444', foreground='#ccc', padding=(10, 5))
    style.configure('TLabel', background='#333', foreground='#ccc')
    style.map('TButton', background=[('active', '#555')])

    frame = ttk.Frame(root, padding=(20, 10))
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Paso 5: Crear el gráfico de dispersión con la línea de regresión
    fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
    ax.scatter(y, predicciones, label='Datos')
    ax.set_xlabel('Datos reales')
    ax.set_ylabel('Predicciones')
    ax.set_title(f'Regresión lineal\nCoeficiente de Pearson: {coeficiente_pearson:.4f}')

    # Integrar el gráfico en la interfaz de usuario de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=0, column=0, pady=10)

    # Botón para cerrar la ventana
    boton_cerrar = ttk.Button(frame, text="Cerrar", command=root.destroy)
    boton_cerrar.grid(row=1, column=0)

    # Ejecutar la interfaz gráfica
    root.mainloop()

# Paso 6: Ejecutar el proceso completo al llamar a la función
cargar_analizar_mostrar()
