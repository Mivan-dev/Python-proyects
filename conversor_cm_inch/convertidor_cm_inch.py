import pandas as pd

def cm_a_inch(cm):
    return cm/2.54

# Leer archivo excel

df = pd.read_excel('mesa_medidas_cm.xlsx')

# Añade columna en inch al DataFrame

df["Pulgadas largo"] = df["Cm largo:"].apply(cm_a_inch)

df["Pulgadas ancho"] = df["Cm ancho:"].apply(cm_a_inch)

df.to_excel('mesa_medidas_cm_inch.xlsx', index=False)

print("Conversion exitosa. Nueva tabla creada.")

