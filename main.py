#Librerias utilizadas:
from fastapi import FastAPI
from fastapi.responses import HTMLResponse #Utilizado para generar el formato de texto de la pagina de inicio 
import pandas as pd
from dateutil import parser
import calendar
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#Creacion de la APP
app = FastAPI(title = "Proyecto Individual 1", description = "Proyecto individual 1 de Data Science")

#Carga de base de datos de las peliculas, con las transofrmaciones ya realizadas.
df_data = pd.read_csv("Datasets/movies_general.csv", low_memory=False, encoding="utf-8")

#Creamos un directorio index con mensaje de bienvenida
@app.get("/", response_class=HTMLResponse)
async def index():
    output = """¡Bienvenido a la interfaz de consultas del catálogo de películas¡
    <br> Las consultas que se pueden realizar son: 
    <br>Consulta 1: Por medio de la ingestión de un dato alfanumérico que identifique un mes, se obtiene el 
    total de películas estrenadas en ese mes.
    <br>Consulta 2: Por medio de la ingestión de un dato alfanúmerico que identifique un día, se obtiene el 
    total de películas estrenadas en ese dia de la semana.
    <br>Consulta 3: Por medio de la ingestión de un dato correspondiente a una franquicia, se obtiene el 
    total de películas de la franquicia, la ganancia total y el promedio de ganancias por película.
    <br>Consulta 4: Por medio de la ingestión de un dato correspondiente a un país, se retorna la cantidad
    de peliculas producidas en ese país y la ganancia generada por estas.
    <br>Consulta 5: Por medio de la ingestión de un dato correspondiente a una productora, se retorna la cantidad
    de películas producidas en ese país.  
    <br>Consulta 6: Por medio de la ingestión de un dato correspondiente a una película, se retorna la inversión,
    las ganancias totales, el retorno y el año de estreno.
    <br> <br>Para conocer el formato de busqueda, consulte el archivo README.md ubicado en el 
    repositorio de GitHub"""
    return output#f'Haga su consulta relacionada a las distitnas plataformas de Streaming'



@app.get("/get_peliculas_mes/")

# Se definió una función llamada peliculas_mes que recibe como argumento 
# el nombre de un mes (en forma de cadena de texto) o un número de mes (como entero). 
# La función devuelve la cantidad de películas que se estrenaron históricamente en ese mes.

def peliculas_mes(month:str or int):
    ''' Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    
    # Se definió un diccionario months que mapea los nombres abreviados de los meses en español a sus números correspondientes. 
        
    months = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 
             'may': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12}
    

    # Se definió una función interna llamada "mes_a_numero" que convierte un nombre de mes (ya sea como cadena de texto o abreviado) 
    # en su número correspondiente. Utiliza la biblioteca dateutil.parser para analizar la cadena de texto y extraer 
    # el número de mes. Si la cadena de texto no se puede analizar, busca en el diccionario months para obtener el número de mes correspondiente al nombre abreviado.

    def mes_a_numero(mes_string):
        try:
            mes = parser.parse(mes_string).month
        except ValueError:
            mes = months.get(mes_string[:3].lower(), None)
        return mes

    # Intenta convertir el argumento month en un número de mes entero. Si no se puede convertir, llama a la función mes_a_numero para obtener el número de mes 
    # correspondiente al nombre de mes proporcionado.

    try:
        month_number = int(month)
    except:
        month_number = mes_a_numero(month)

    # Se realizó un filtro en el dataframe df_data para obtener las filas correspondientes al mes dado. Utiliza la columna 
    # "release_month" del dataframe y compara los valores con el número de mes.    

    df_mov_month = df_data[ df_data["release_month"].astype(int) == month_number]

    # Se calculó la cantidad de películas en el mes filtrado utilizando la función shape[0] del dataframe resultante.
    
    cant_pel_month = df_mov_month.shape[0]

    # Se definió una función interna get_month_name que recibe un número de mes y devuelve el nombre del mes en español. 
    # Utiliza un diccionario months_es para mapear los números de mes a sus nombres correspondientes en español.
    
    def get_month_name(month):
        months_es = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
        }
        month_name = months_es.get(month, "Mes inválido")
        return month_name
    
    return "La cantidad de peliculas en el mes de "+get_month_name(month_number)+" son de "+ str(cant_pel_month)


@app.get("/peliculas_dia/")

#  Se definió una función llamada peliculas_dia, que recibe como argumento un día de la semana (ya sea en forma de cadena de
#  texto o como un número) y devuelve la cantidad de películas que se estrenaron en ese día de la semana históricamente.

def peliculas_dia(day:str or int):
    '''Se ingresa el dia y la funcion retorna la cantidad de 
    peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') 
    historicamente''' 

    # Se definió una función interna llamada convert_day, 
    # que se encarga de convertir el día proporcionado en una representación estandarizada en español.

    def convert_day(day_string):
        
        # Se creo un diccionario un diccionario dias_semana que mapea abreviaturas de días a los nombres 
        # completos de los días en español

        dias_semana = {
            'lun': 'lunes',
            'mar': 'martes',
            'mie': 'miércoles',
            'jue': 'jueves',
            'vie': 'viernes',
            'sab': 'sábado',
            'dom': 'domingo'
        }

        # Si el usuario proporciona un número, se verifica primero si es mayor a 7, si es mayor se realiza una operación
        # pestá en el rango válido (1-7), calculando el residuo. Luego se verifica que este en un rango entre (1-7) y
        # se utiliza para obtener el nombre del día correspondiente. Si se proporciona una cadena de texto, 
        # se busca una coincidencia con las abreviaturas de los días en el diccionario dias_semana y se devuelve el nombre 
        # completo del día correspondiente. Si no se puede convertir el día, se retorna None

        if day_string.isdigit():
            dia_numero = int(day_string)
            if dia_numero > 7:
               dia_numero = (dia_numero - 1) % 7 + 1
            if dia_numero >= 1 and dia_numero <= 7:
                return list(dias_semana.values())[dia_numero - 1]
            
        else:
            day_string = day_string.lower()[:3]
            for dia_abrev, day_complet in dias_semana.items():
                if dia_abrev.startswith(day_string):
                    return day_complet
        
        return None   
    
    # Se llama la funcion "convert_day" para obtener el nombre del día de la semana en español.

    day_convert = convert_day(day)

    # Si se obtiene un resultado válido, se asigna a la variable day_convert y se continúa con el procesamiento. 
    # En caso contrario, se imprime un mensaje de "Entrada inválida".

    if day_convert:
        day_week = day_convert
    else:
        print("Entrada inválida.")

    # Se filtra el dataframe df_data para obtener las filas correspondientes al día de la semana especificado. 
    
    df_mov_day = df_data[ df_data["day"] == day_week]

    # Se cuenta el número de filas resultantes y se guarda en la variable "cant_pel_day".

    cant_pel_day = df_mov_day.shape[0]

    
    return "La cantidad de peliculas que historicamente se estrenaron el día "+day_convert+" son de "+ str(cant_pel_day)


@app.get("/franquicia/")

# Se definió una función llamada franquicia que recibe como argumento el nombre de una franquicia.

def franquicia(franquicia:str): 
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' 

    # Se obtienen los valores unicos de las franquicias que estan en el dataframe original.

    franq_options = df_data["NameCollection"].unique()

    # En base a lo ingresado por el usuario se extrae la que mas coincidencias tenga.

    close_option = process.extractOne(franquicia, franq_options)[0]

    # Se filtran las filas del dataframe que corresponden a la franquicia cercana encontrada.

    df_result = df_data[df_data["NameCollection"] == close_option]

    # Calcula la cantidad de películas de la franquicia encontrada.

    amount_movies = df_result.shape[0]

    # Calcula la ganancia total de la franquicia sumando la columna 

    profit = df_result["revenue"].sum()-df_result["budget"].sum()

    # Calcula el promedio de ganancias por película dividiendo la 
    # ganancia total entre la cantidad de películas del DataFrame filtrado

    ave_profit = profit/df_result.shape[0]   
    
    return {'franquicia':close_option, 'cantidad':amount_movies, 'ganancia_total':profit, 'ganancia_promedio':round(ave_profit,2)}

@app.get("/peliculas_pais")

# Se definio unaa función denominada peliculas_pais que recibe como argumento el nombre de un país y retorna la 
# cantidad de películas  producidas en ese país.

def peliculas_pais(country:str): 
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' 
    
    # Se filtraron las columnas que contienen en su nombre la palabra "Country" y se crea una lista para almacenar resultados.

    country_colums = df_data.filter(like="Country").columns

    results = []

    # Se itera sobre cada columna obtenida en el filtro.
    
    for columna in country_colums:

        # Para cada columna, se obtienen los valores únicos que no son nulos y se realiza una comparación utilizando la función process.extractOne() 
        # para encontrar la mejor coincidencia entre el país ingresado y los valores únicos de la columna

        options = df_data[columna].dropna().unique()

        best_coinci = process.extractOne(country, options)

        # Si se encuentra una coincidencia con una puntuación igual o superior al 90, se agrega el resultado a la lista "results" y 
        # se guarda el país coincidente en la variable "country_output".
    
        if best_coinci is not None and best_coinci[1] >= 90:
            results.append(best_coinci[0])
            country_output = best_coinci[0]

    # Si se obtuvieron resultados coincidentes en el paso anterior, se filtran las filas del DataFrame "df_data" que contengan 
    # al menos uno de los países coincidentes en alguna de las columnas de país.
    if results:
        df_results = df_data[df_data.isin(results).any(axis=1)]
    else:
        print("No se encontraron coincidencias para la palabra clave ingresada.")

    # Se calcula la cantidad de películas en el DataFrame filtrado utilizando el atributo "shape".

    count_mov = df_results.shape[0]

    return {'pais':country_output, 'cantidad':count_mov}


@app.get("/peliculas_productora/")

# Se definio unaa función denominada "productoras" que recibe como argumento el nombre de una compañia productora y retorna la 
# cantidad de películas producidas por esa compañia

def productoras(company:str): 
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' 
    
    # Se obtienen las columnas del DataFrame df_data que contienen la palabra "NameCompany" en su nombre y se inicializa una lista.
    
    company_colums = df_data.filter(like="NameCompany").columns

    results = []


    # Se itera sobre cada columna obtenida en el paso anterior.

    for columna in company_colums:

        # Para cada columna, se obtienen los valores únicos que no son nulos y se realiza una comparación utilizando la función "process.extractOne".
        options = df_data[columna].dropna().unique()
        best_coinci = process.extractOne(company, options)

        # Si se encuentra una coincidencia con una puntuación igual o superior al 90, se agrega el resultado a la lista "results" y se guarda el
        # nombre de la compañía coincidente en la variable "company_output".
        if best_coinci is not None and best_coinci[1] >= 90:
            results.append(best_coinci[0])
            company_output = best_coinci[0]

    # Si se obtuvieron resultados coincidentes en el paso anterior, se filtran las filas del DataFrame "df_data" que contengan al menos uno de los 
    # nombres de compañía coincidentes en alguna de las columnas de compañía
    if results:
        df_result = df_data[df_data.isin(results).any(axis=1)]
    else:
        print("No se encontraron coincidencias para la palabra clave ingresada.")

    # Se calcula la cantidad de películas en el DataFrame filtrado utilizando el atributo "shape".
    count_mov_company = df_result.shape[0]

    # Se calcula la ganancia total de las películas en el DataFrame filtrado sumando la columna "revenue"
    profit = df_result["revenue"].sum()

    return {'productora ':company_output, 'ganancia_total ':profit, ' cantidad ':count_mov_company}

@app.get("/retorno_pelicula/")

# Se definió una función denominada "retorno", la toma el nombre de una película como entrada y devuelve información relacionada con la película.
def retorno(movie:str): 
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' 
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' 
  
    # Se obtienen los valores unicos de las franquicias que estan en el dataframe original
    unique_movie = df_data["title"].unique()

    # En base a lo ingresado por el usuario se extrae la que mas coincidencias tenga
    close_option = process.extractOne(movie, unique_movie)[0]

    # Filtrar las filas del dataframe que corresponden a la franquicia cercana encontrada
    df_result = df_data[df_data["title"] == close_option]
    

    return {'pelicula':close_option, 'inversion':  int(df_result["budget"]), 'ganacia':  int(df_result["revenue"]),'retorno':  int(df_result["return"]), 'anio':int(df_result["release_year"])} 