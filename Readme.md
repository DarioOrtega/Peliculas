<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

## **Descripción del proyecto**

## Contexto

Se contaba con una base de datos de peliculas, las cual debia ser tratada, realizando un análisis exploratorio de datos (EDA), para posteriormente, generar una serie de consultas sobre la misma. 


## Desarrollo

Para el desarrollo del proyecto se siguió la ruta marcada en la siguiente figura:

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=500>
</p>


**`Transformaciones`**:  En este paso se empezó por análizar el contenido del archivo .xlsx, observando su contenido. Posterior a esto, se llevaron a cabo las siguientes transformaciones, las cuales se encuentran en archivo `transformaciones.ipny`:

+ Los campos **`belongs_to_collection`**, **`genres`**, **`production_companies`**, **`production_countries`**  y **`spoken_languajes`** estaban anidados, tenian un diccionario o una lista como valores en cada fila, por lo tanto se desanidaron y posteriormente se unieron en un nuevo datasets para su posterior uso en las consultas propuestas. 

+ Los valores nulos de los campos **`revenue`**, **`budget`** se rellenaron por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** se eliminaron.

+ Se modificaron las fechas para tener el formato **`AAAA-mm-dd`**, eliminando algunos filas que contenian datos incorrectos, creando la columna **`release_year`** donde se extrajo el año de la fecha de estreno.

+ Se creó la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hubó datos disponibles para calcularlo, se tomó el valor **`0`**.

+ Así mismo, se eliminaron las columnas que no iban a ser utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`vote_count`**,**`poster_path`** y **`homepage`**.

<br/>

**`Desarrollo API`**:  Para el desarrollo del API, se utilizó el framework el framework ***FastAPI***. Las consultas que propuestas son las siguientes:

  
+ def peliculas_mes(mes):
    ''' Donde el usuario ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente'''
    return {'mes':mes, 'cantidad':respuesta}

+ def peliculas_dia(dia):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente'''
    return {'dia':dia, 'cantidad':respuesta}

+ def franquicia(franquicia):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

+ def peliculas_pais(pais):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    return {'pais':pais, 'cantidad':respuesta}

+ def productoras(productora):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''
    return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

+ def retorno(pelicula):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}



<br/>


**`Deployment`**:  Para el deployment de la API se utilizo la red de servicios [Render](https://render.com/docs/free#free-web-services), utilizando como tutorial el proporcionado en [Tutorial de Render](https://github.com/HX-FNegrete/render-fastapi-tutorial). En este [link](https://pi1-huzk.onrender.com/docs#/) se puede observar el deployment del API. 

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Después de las transformaciones realizadas inicialmente, se realizo un pequeño EDA, observando las relaciones entre las diferentes variables de los datasets, buscando outliers o anomalías. Para este análisis se hizó uso de la libreria matplotlib y seaborn, observando el comportamiento de algunas variables por medio de pairplot y la matriz de correlación de Pearson. El desarrollo de este análisis se encuentra en el archivo `EDA.py`. Se creo una nube de palabras por medio de la libreria Wordcloud.

**`Sistema de recomendación`**: 

Éste sistema de recomendación consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se encuentra la similitud de puntuación entre esa película y el resto de películas, ordenandose según el score de similaridad y devolviendo una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Esta funcion se encuentra ser deployado en la [API](https://pi1-huzk.onrender.com/docs#/) y se llama recomendación.


**`Video`**: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!



