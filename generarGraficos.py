import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Asegurar que la carpeta de salida exista
os.makedirs("static", exist_ok=True)

# Cargar el dataset
df_csv = pd.read_csv("Streaming_dataset.csv")


# 1. Frecuencia de calificaciones (Barras)
df_csv['Calificación Agrupada'] = df_csv['Calificación Promedio /5'].round(1)
conteo_calificacion = df_csv['Calificación Agrupada'].value_counts().sort_index()
conteo_calificacion_df = conteo_calificacion.reset_index()
conteo_calificacion_df.columns = ['Calificación', 'Frecuencia']

plt.figure(figsize=(12, 6))
colors = sns.color_palette('seismic', n_colors=len(conteo_calificacion_df))
sns.barplot(
    data=conteo_calificacion_df,
    x='Calificación',
    y='Frecuencia',
    hue='Calificación',
    palette=colors,
    legend=False
)
plt.title("Frecuencia de Calificaciones Promedio por Plataforma")
plt.xlabel("Calificación Promedio /5")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("static/calificaciones_frecuencia.png")
plt.close()


# 2. Histograma de ingresos anuales

plt.figure(figsize=(10, 6))
plt.hist(df_csv['Ingresos Anuales (millones)'], bins=11, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Histograma de Ingresos Anuales (millones)')
plt.xlabel('Ingresos Anuales (millones)')
plt.ylabel('Frecuencia')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("static/ingresos_histograma.png")
plt.close()


# 3. Boxplot simple: Tiempo Usado

plt.figure(figsize=(12, 6))
sns.boxplot(x=df_csv['Tiempo Usado (horas)'], color='cyan')
plt.title('Distribución de Tiempo Usado (horas)')
plt.xlabel('Tiempo Usado (horas)')
plt.tight_layout()
plt.savefig("static/tiempo_uso_boxplot.png")
plt.close()


# 4. Boxplot múltiple: Ingresos por Plataforma

plt.figure(figsize=(12, 6))
colors = sns.color_palette('seismic', df_csv['Ingresos Anuales (millones)'].nunique())
sns.boxplot(
    x=df_csv['Plataforma'],
    y=df_csv['Ingresos Anuales (millones)'],
    data=df_csv,
    palette=colors,
    hue='Plataforma',
    legend=False
)
plt.title('Distribución de Ingresos Anuales (millones) por Plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Ingresos Anuales (millones)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("static/ingresos_boxplot_plataforma.png")
plt.close()


# 5. Mapa de calor de correlaciones

corr_mat = df_csv.corr(numeric_only=True)
plt.figure(figsize=(12, 6))
sns.heatmap(corr_mat, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlación entre Variables Numéricas')
plt.tight_layout()
plt.savefig("static/matriz_correlacion.png")
plt.close()

print(" Gráficos generados y guardados correctamente en la carpeta 'static/'.")
