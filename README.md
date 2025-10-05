
# Analisis_Educativo

Bienvenido/a — este repositorio contiene una pequeña herramienta en Python para analizar encuestas sobre hábitos de estudio y generar reportes visuales en HTML. La documentación está escrita en un tono cercano y práctico, como si te lo explicara un colega (corto, claro y con ejemplos).

## Qué hace este proyecto

- Carga un CSV con respuestas de estudiantes.
- Limpia y normaliza las columnas más relevantes (edad, horas de estudio, método, distractores, etc.).
- Calcula análisis descriptivos y comparativos: promedio por método, impacto de distractores, correlaciones, entre otros.
- Genera gráficos y un reporte HTML listo para compartir.
- Incluye una interfaz gráfica (basada en customtkinter) para seleccionar el CSV, elegir secciones y exportar el HTML.

Siéntete libre de usarlo como plantilla o adaptarlo para tus propios datos.

## Estructura del repositorio

- `main.py` - Script principal de ejemplo (CLI) que muestra la secuencia de uso: carga, exploración, limpieza y algunos análisis.
- `prueba.csv` - CSV de ejemplo (si lo tienes) para probar el flujo.
- `requirements.txt` - Dependencias del proyecto.
- `README.md` - Este archivo.
- `src/` - Código fuente dividido en módulos:
	- `analisis_datos.py` - Funciones que realizan los análisis estadísticos y agregaciones.
	- `procesamiento.py` - Funciones para explorar y limpiar el DataFrame.
	- `generar_html.py` - Construye gráficas y arma un reporte HTML con las observaciones y KPIs.
	- `graficos.py` - Funciones auxiliares para graficar (devuelven figuras matplotlib).
	- `interfaz.py` - Aplicación GUI con `customtkinter` para generar reportes sin usar la terminal.
	- `img/` - Imágenes usadas por la interfaz.

## Requisitos

Instala las dependencias (recomendado en un entorno virtual):

```
pip install -r requirements.txt
```

Dependencias principales:
- pandas
- numpy
- matplotlib
- seaborn
- Pillow
- customtkinter

## Formato esperado del CSV

El flujo estándar espera un CSV con columnas que serán renombradas internamente a las siguientes (en el orden que el archivo original tenga las columnas):

1. `edad_alumno` - Edad (numérica)
2. `curso_alumno` - Curso o grado (texto)
3. `horas_estudiadas` - Horas declaradas (numéricas)
4. `horario_fijo` - Sí/No o descriptor (texto)
5. `frecuencia_repaso` - Por ejemplo: DIARIO, SEMANAL, etc. (texto)
6. `metodo_estudio` - Método utilizado (texto)
7. `escala_promedio` - Promedio académico (numérico)
8. `promedio_reflejo` - (opcional) respuesta espejo (texto)
9. `principales_distractores` - Texto con distractor principal
10. `recursos_estudios` - Recurso de estudio preferido (texto)
11. `sentimientos_respecto_estudio` - Emoción o sentimiento (texto)
12. `motivacion_estudio` - Nivel de motivación (texto)

Si tu CSV tiene una columna llamada `Marca temporal`, el limpiador la eliminará automáticamente.

Si no quieres renombrar manualmente, el código intentará renombrar las columnas según el orden. Si el número de columnas no coincide, `procesamiento.limpiar_datos()` emitirá una advertencia y devolverá el DataFrame sin renombrar.

Consejo rápido: abre el CSV en un editor y verifica el orden o añade una línea que imprima `df.columns` antes de limpiar.

## Cómo usar

1) Uso por línea de comandos (ejemplo con `main.py`):

```
python main.py
```

El `main.py` es un ejemplo que carga `data/prueba.csv`, ejecuta exploración, limpieza y muestra algunos resultados por consola.

2) Interfaz gráfica

- Ejecuta `src/interfaz.py` o empaqueta con PyInstaller si quieres un ejecutable.
- La interfaz permite seleccionar el CSV, la carpeta de destino, marcar qué secciones incluir en el HTML y generar el reporte.

3) Usar las funciones desde Python

Ejemplo mínimo:

```python
import pandas as pd
from src.procesamiento import limpiar_datos
from src.generar_html import generar_reporte_html

df = pd.read_csv('ruta/a/tu.csv')
df_limpio = limpiar_datos(df)
generar_reporte_html(df_limpio, 'salida/reporte.html')
```

## Módulos y funciones importantes

- `procesamiento.explorar_datos(df)`
	- Imprime info, estadísticas descriptivas y conteo de nulos.

- `procesamiento.limpiar_datos(df)`
	- Renombra columnas, normaliza texto (mayúsculas y trim), convierte columnas numéricas y crea la columna `rango_horas`.

- `analisis_datos` (varias funciones)
	- `analisis_promedio_por_metodo(df)` -> promedio, cuenta y desviación por método.
	- `analisis_horas_vs_promedio(df)` -> calcula y muestra correlación entre horas y promedio.
	- `analisis_distractores(df)` -> promedio por distractor.
	- Y otras funciones auxiliares para motivación, recursos, frecuencia de repaso, etc.

- `generar_html.generar_reporte_html(df, ruta_salida, incluir=None, nombre_html=None)`
	- Genera un HTML con KPIs, gráficos embebidos y observaciones automáticas.
	- `incluir` es una lista de claves para seleccionar secciones (por ejemplo `['horas','promedio_metodo']`).

- `interfaz.ExportedApp` (GUI)
	- Pantalla para seleccionar CSV, carpeta destino, nombre opcional del HTML y secciones a incluir.

## Buenas prácticas y notas

- Si vas a procesar muchos archivos o datos grandes, convierte primero las columnas numéricas con `pd.to_numeric(..., errors='coerce')` y verifica los nulos.
- Las funciones del módulo `analisis_datos` devuelven DataFrames o estructuras ligeras; puedes guardarlas con `to_csv()` si quieres conservar tablas intermedias.
- El generador de HTML convierte figuras matplotlib a base64 y las inserta inline; ten en cuenta que archivos muy grandes generan HTML pesados.

## Depuración rápida

- Si el HTML sale en blanco o sin secciones, revisa que las columnas clave estén presentes y que hayas marcado secciones en la GUI.
- Mensajes comunes:
	- "ADVERTENCIA: Tu CSV tiene X columnas..." -> revisa el orden/estructura del CSV.
	- Errores al abrir imágenes en la GUI -> asegúrate de que `img/` y `python.ico` estén presentes.

## Tests rápidos

Para verificar que el entorno está bien:

```
python -c "import pandas; import numpy; import matplotlib; import seaborn; print('OK')"
```