import pandas as pd

def tipo_dato_x_columna(tabla: pd.DataFrame) -> pd.DataFrame:
    tipos = tabla.dtypes.reset_index()
    tipos.columns = ['columna', 'tipo']
    return tipos

def nulos_x_columna(tabla: pd.DataFrame) -> pd.DataFrame:
    cantidad_nulos = tabla.isnull().sum().reset_index()
    cantidad_nulos.columns = ['columna', 'cantidad de valores nulos']
    return cantidad_nulos

def unicos_x_columna(tabla: pd.DataFrame) -> pd.DataFrame:
    cantidad_nulos = tabla.nunique().reset_index()
    cantidad_nulos.columns = ['columna', 'cantidad de valores unicos']
    return cantidad_nulos