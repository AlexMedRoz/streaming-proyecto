from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    graficos = [
        {
            "titulo": "Frecuencia de Calificaciones",
            "imagen": "calificaciones_frecuencia.png",
            "descripcion": "Muestra cuántas veces se repite cada calificación promedio."
        },
        {
            "titulo": "Histograma de Ingresos Anuales",
            "imagen": "ingresos_histograma.png",
            "descripcion": "Distribución de los ingresos anuales de cada plataforma."
        },
        {
            "titulo": "Boxplot de Tiempo Usado",
            "imagen": "tiempo_uso_boxplot.png",
            "descripcion": "Muestra la dispersión del tiempo de uso por plataforma."
        },
        {
            "titulo": "Boxplot de Ingresos por Plataforma",
            "imagen": "ingresos_boxplot_plataforma.png",
            "descripcion": "Comparación de ingresos anuales entre plataformas."
        },
        {
            "titulo": "Mapa de Correlación",
            "imagen": "matriz_correlacion.png",
            "descripcion": "Visualiza la relación estadística entre variables numéricas."
        }
    ]
    return render_template("index.html", graficos=graficos)

if __name__ == "__main__":
    print("Servidor Flask iniciando...")
    app.run(debug=True)
