import sys
import os

# Incluir carpeta "src"
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pandas as pd
from procesamiento import explorar_datos, limpiar_datos
from analisis_datos import (
    analisis_promedio_por_metodo, analisis_horas_vs_promedio, analisis_distractores
)

if __name__ == "__main__":
    ruta_csv = os.path.join('data', 'prueba.csv')
    try:
        df = pd.read_csv(ruta_csv)
        print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{ruta_csv}'")
        exit(1)

    explorar_datos(df)
    df_limpio = limpiar_datos(df)
    print(df_limpio.head())

    print(analisis_promedio_por_metodo(df_limpio))
    analisis_horas_vs_promedio(df_limpio)
    print(analisis_distractores(df_limpio))