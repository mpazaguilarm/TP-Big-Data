# Instalo pandas, matplotlib, numpy y openpyxl con "python3 -m pip install pandas openpyxl numpy matplotlib" en la terminal
# Importar pandas
import pandas as pd
#importo el set de datos que voy a usar: la EPH
file_path = "/Users/pazaguilarm/Documents/usu_individual_T424.xlsx"

# Cargar el archivo Excel usando pandas y openpyxl
data = pd.read_excel(file_path, engine='openpyxl')


data_filtrada = data[["CH04", "CH06", "CH08", "NIVEL_ED", "ESTADO", "CAT_INAC", "PP08D1"]]  

# Chequear si hay datos faltantes en las columnas de nuestro dataset filtrado
print(data_filtrada.isnull().sum())

# Eliminar filas con datos faltantes
data_filtrada = data_filtrada.dropna()

# Visualizar los primeros registros del dataset filtrado y sin valores nulos
print(data_filtrada.head())
 # Renombro las columnas para que sean mas faciles de usar
data_filtrada.rename(columns={
    "CH04": "Sexo",
    "CH06": "Edad",
    "CH08": "CoberturaMedica",
    "NIVEL_ED": "NivelEducativo",
    "ESTADO": "EstadoActividad",
    "CAT_INAC": "CategoriaInactividad",
    "PP08D1": "Salario"
}, inplace=True)
# Verifico que se hayan renombrado bien
print(data_filtrada.head())

# Arranco a trabajar con los datos
# Primero, vamos a analizar diferencias en el empleo entre hombres y mujeres
# Que porcentage de las mujeres y de los hombres son empleados asalariuados (pie chart)
# Que porcentage desempleado? (pie chart)
# Salario promedio de cada uno (en numeros)
# Salario por edad de cada uno (grafico continuo tipo normal o histograma)