import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 4.1. Introducción a NumPy
def introduccion_numpy():
    print("Introducción a NumPy:")
    array = np.array([1, 2, 3, 4, 5])
    print("Array de NumPy:", array)
    print()

# 4.2. Operaciones avanzadas con matrices NumPy
def operaciones_avanzadas_numpy():
    print("Operaciones avanzadas con matrices NumPy:")
    matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Matriz original:\n", matriz)
    print("Transpuesta:\n", matriz.T)
    print("Suma de todos los elementos:", np.sum(matriz))
    print("Determinante de la matriz:", np.linalg.det(matriz))
    print()

# 4.3. Introducción a Pandas
def introduccion_pandas():
    print("Introducción a Pandas:")
    data = {'Nombre': ['Ana', 'Luis', 'Pedro', 'Marta'],
            'Edad': [28, 34, 29, 42],
            'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}
    df = pd.DataFrame(data)
    print("DataFrame de Pandas:\n", df)
    print()

# 4.4. Manipulación de datos en Pandas DataFrames
def manipulacion_datos_pandas():
    print("Manipulación de datos en Pandas DataFrames:")
    data = {'Nombre': ['Ana', 'Luis', 'Pedro', 'Marta'],
            'Edad': [28, 34, 29, 42],
            'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']}
    df = pd.DataFrame(data)
    print("DataFrame original:\n", df)
    df['Edad'] = df['Edad'] + 1
    print("DataFrame después de incrementar la edad:\n", df)
    print()

# 4.5. Visualización básica de datos con Seaborn
def visualizacion_basica_seaborn():
    print("Visualización básica de datos con Seaborn:")
    tips = sns.load_dataset('tips')
    sns.scatterplot(data=tips, x='total_bill', y='tip')
    plt.title("Propinas vs Total de la Cuenta")
    plt.show()

# 4.6. Visualización avanzada de datos con Seaborn
def visualizacion_avanzada_seaborn():
    print("Visualización avanzada de datos con Seaborn:")
    tips = sns.load_dataset('tips')
    sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex', markers=['o', 'x'])
    plt.title("Propinas vs Total de la Cuenta con Regresión Lineal")
    plt.show()

def main():
    introduccion_numpy()
    operaciones_avanzadas_numpy()
    introduccion_pandas()
    manipulacion_datos_pandas()
    visualizacion_basica_seaborn()
    visualizacion_avanzada_seaborn()

if __name__ == "__main__":
    main()
