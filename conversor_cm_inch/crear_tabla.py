import pandas as pd

# Data frame es la info de las piezas y sus medidas.

data = {
    "Piezas:": ["Patas", "Travesaños", "Tapa", "Cajon"],
    "Cm largo:": ["70", "110", "120", "60"],
    "Cm ancho:": ["10", "10", "80", "40"]
}

df = pd.DataFrame(data)

# Guarda el DataFrame en excel

df.to_excel("mesa_medidas_cm.xlsx", index=False)