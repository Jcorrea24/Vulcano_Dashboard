import pandas as pd

def leer_csv(ruta):
    try:
        df = pd.read_csv(ruta, sep=';')

        print("Archivo cargado correctamente")
        print(df.head())

        return df

    except Exception as e:
        print("Error leyendo archivo:", e)