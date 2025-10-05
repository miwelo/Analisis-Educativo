import sys
import os

# Asegura que src/ esté en el path para los imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pandas as pd
from procesamiento import explorar_datos, limpiar_datos
from analisis_datos import (
    analisis_promedio_por_metodo, analisis_horas_vs_promedio, analisis_distractores
)

if __name__ == "__main__":
    # 1. Cargar datos
    ruta_csv = os.path.join('data', 'prueba.csv')
    try:
        df = pd.read_csv(ruta_csv)
        print(f"✅ Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    except FileNotFoundError:
        print(f"❌ ERROR: No se encontró el archivo '{ruta_csv}'")
        exit(1)

    # 2. Exploración inicial
    explorar_datos(df)

    # 3. Limpieza de datos
    df_limpio = limpiar_datos(df)
    print("\n📊 Primeras filas del dataset limpio:")
    print(df_limpio.head())

    # 4. Análisis exploratorio
    print("\n📈 Análisis por Método de Estudio:")
    print(analisis_promedio_por_metodo(df_limpio))
    analisis_horas_vs_promedio(df_limpio)
    print("\n📈 Análisis de Distractores:")
    print(analisis_distractores(df_limpio))

    # 5. (Eliminado: Generar reporte PDF)