from google.colab import files
import pandas as pd
import numpy as np
def cramer_method(matrix_A, matrix_B):
    det_A = np.linalg.det(matrix_A)

    solutions = []

    for i in range(matrix_A.shape[1]):
        matrix_temp = matrix_A.copy()
        matrix_temp[:, i] = matrix_B
        det_temp = np.linalg.det(matrix_temp)
        solution = det_temp / det_A
        solutions.append(solution)

    return solutions

# Pide al usuario que cargue el archivo Excel
uploaded = files.upload()

# Obtiene el nombre del archivo cargado
file_name = list(uploaded.keys())[0]

# Lee el archivo Excel
try:
    df = pd.read_excel(file_name, header=None)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Verifica que la matriz es cuadrada (número de filas = número de columnas)
if df.shape[0] != df.shape[1]:
    print("La matriz no es cuadrada. El método de Cramer solo se aplica a matrices cuadradas.")
    exit()

# Pide al usuario que ingrese la matriz B
matrix_B_values = input("Ingrese los valores de la matriz B separados por espacios: ")
matrix_B = np.array([float(value) for value in matrix_B_values.split()])

# Convierte el DataFrame a una matriz NumPy
matrix_A = df.to_numpy()

# Resuelve el sistema de ecuaciones usando el método de Cramer
solutions = cramer_method(matrix_A, matrix_B)

# Muestra las soluciones
print("Soluciones:")
for i, sol in enumerate(solutions):
    print(f"x{i + 1} = {sol}")