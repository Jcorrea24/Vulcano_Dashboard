import os
from Backend.lectura import leer_csv
from Backend.limpieza import limpiar_datos
from Backend.analisis import analizar_datos
from Backend.exportar import exportar_csv

def main():
    # 1. Definir rutas de entrada y salida
    ruta_entrada = os.path.join('Data', 'proyecto_integrador_data.csv')
    ruta_salida = os.path.join('Output', 'proyecto_integrador_data_limpio.csv')
    
    print("--- Iniciando Pipeline de Datos ---")
    
    # 2. Leer los datos
    df = leer_csv(ruta_entrada)
    if df is None:
        print("Error: No se pudieron cargar los datos.")
        return
        
    # 3. Limpiar los datos
    df_limpio = limpiar_datos(df)
    
    # 4. Analizar los datos
    analizar_datos(df_limpio)
    
    # 5. Exportar resultados (genera CSV en Output/ y JSON en Frontend/)
    exportar_csv(df_limpio, ruta_salida)
    
    print("--- Pipeline finalizado con exito ---")

if __name__ == '__main__':
    main()
