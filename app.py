import os
from flask import Flask, render_template
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def heatmap():
    # Datos de ejemplo para el mapa de calor
    data = np.random.rand(5, 5)
    
    # Crear el mapa de calor utilizando Seaborn
    sns.heatmap(data, annot=True, cmap='YlOrRd')
    
    # Guardar el mapa de calor en la raíz del proyecto
    heatmap_file = 'heatmap.png'
    plt.savefig(heatmap_file)
    
    # Obtener la ruta absoluta del archivo heatmap.png

if __name__ == '__main__':
    app.run(debug=True)
