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


**`Transformaciones`**:  En este paso se empezó por análizar el contenido del archivo .xlsx, observando su contenido. Posterior a esto, se llevaron a cabo las siguientes transformaciones, las cuales se encuentran en archivo `transformaciones.py`:

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


**`Deployment`**:  Para el deployment de la API se utilizo la red de servicios [Render](https://render.com/docs/free#free-web-services) y tienes un [tutorial de Render](https://github.com/HX-FNegrete/render-fastapi-tutorial) que te hace la vida mas facil :smile: . Tambien podrias usar [Railway](https://railway.app/), o cualquier otro servicio que permita que la API pueda ser consumida desde la web.

<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

Ya los datos están limpios, ahora es tiempo de investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías (que no tienen que ser errores necesariamente :eyes: ), y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. Las nubes de palabras dan una buena idea de cuáles palabras son más frecuentes en los títulos, ¡podría ayudar al sistema de recomendación! Sabes que puedes apoyarte en librerías como _pandas profiling, missingno, sweetviz, autoviz_, entre otros y sacar de allí tus conclusiones 😉

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API, está lista para consumir por los departamentos de Analytics y Machine Learning, y nuestro EDA nos permite entender bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas. El EDA debería incluir gráficas interesantes para extraer datos, como por ejemplo una nube de palabras con las palabras más frecuentes en los títulos de las películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:

+ def recomendacion('titulo'):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores'''
    return {'lista recomendada': respuesta}

<br/>

**`Video`**: Necesitas que al equipo le quede claro que tus herramientas funcionan realmente! Haces un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

<sub> **Spoiler**: El video NO DEBE durar mas de ***7 minutos*** y DEBE mostrar las consultas requeridas en funcionamiento desde la API** y una breve explicacion del modelo utilizado para el sistema de recomendacion. <sub/>

<br/>

## **Criterios de evaluación**

**`Código`**: Prolijidad de código, uso de clases y/o funciones, en caso de ser necesario, código comentado. 

**`Repositorio`**: Nombres de archivo adecuados, uso de carpetas para ordenar los archivos, README.md presentando el proyecto y el trabajo realizado

**`Cumplimiento`** de los requerimientos de aprobación indicados en el apartado `Propuesta de trabajo`

NOTA: Recuerde entregar el link de acceso al video. Puede alojarse en YouTube, Drive o cualquier plataforma de almacenamiento. **Verificar que sea de acceso público**.

<br/>
Aqui te sintetizamos que es lo que consideramos un MVP aprobatorio, y la diferencia con un producto completo.



<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/MVP_MLops.PNG"  height=250>
</p>


## **Fuente de datos**

+ [Dataset](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view?usp=sharing): Archivo con los datos que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>

## **Material de apoyo**

En este mismo repositorio podras encontrar algunos [links de ayuda](hhttps://github.com/HX-PRomero/PI_ML_OPS/raw/main/Material%20de%20apoyo.md). Recuerda que no son los unicos recursos que puedes utilizar!



  
<br/>

## **Deadlines importantes**

+ Apertura de formularios de entrega de proyectos: **Lunes 15, 10:00 hs gmt -3**

+ Cierre de formularios de entrega de proyectos: **Martes 16, 16:00hs gmt-3**
  
+ Demo: **Martes 16, 16:00hs gmt-3*** 
