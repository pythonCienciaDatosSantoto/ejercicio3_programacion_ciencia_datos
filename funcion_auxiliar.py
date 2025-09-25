import pandas as pd
import requests

def load_data_from_api(limit: int = 50000) -> pd.DataFrame:
    """
    Carga datos desde la API de Socrata (Datos Abiertos Colombia) en formato JSON 
    y los convierte en un DataFrame de pandas.

    Args:
        limit (int): Número máximo de registros a solicitar. Por defecto es 50,000.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados. Si ocurre un error, 
                      devuelve un DataFrame vacío.
    """
    # URL del dataset de Matrícula en Educación Básica y Media por municipio para el año 2021
    api_url = f"https://www.datos.gov.co/resource/nudc-7mev.json?$limit={limit}"
    
    try:
        # Realizar la petición GET a la API
        response = requests.get(api_url)
        # Generar un error si la respuesta HTTP no es exitosa (ej. 404, 500)
        response.raise_for_status()
        
        # Convertir la respuesta JSON a una lista de diccionarios
        data = response.json()
        
        # Crear un DataFrame de pandas a partir de los datos
        df = pd.DataFrame(data)
        
        print(f"Se cargaron {len(df)} registros exitosamente.")
        return df
        
    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión, timeout, o respuestas HTTP erróneas
        print(f"Error de conexión o al consultar la API: {e}")
        
    except Exception as e:
        # Manejar otros errores inesperados (ej. JSON mal formado)
        print(f"Ocurrió un error inesperado: {e}")
        
    # Retornar un DataFrame vacío si cualquier parte del proceso falla
    return pd.DataFrame()

# Ejemplo de uso (puedes ejecutar este script directamente para probar)
if __name__ == "__main__":
    df_educacion = load_data_from_api()
    if not df_educacion.empty:
        print("\nPrimeras 5 filas del DataFrame:")
        print(df_educacion.head())
        print("\nInformación del DataFrame:")
        df_educacion.info()
