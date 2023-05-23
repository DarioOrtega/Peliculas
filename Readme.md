<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

## **Descripción del proyecto**

## Contexto

Se contaba con una base de datos de peliculas, las cual debia ser tratada, realizando un análisis exploratorio de datos (EDA), para posteriormente, generar una serie de consultas sobre la misma. 


## Desarrollo

Para el desarrollo del proyecto se siguieron los siguientes pasos:

Análisis Exploratorio de los datos (Exploratory Data Analysis = EDA)

Se realizo un EDA, observando las relaciones entre las diferentes variables del dataset. Para este análisis se hizó uso de la libreria matplotlib,  pandas, seaborn y wordcloud, por medio de las cuales se observó el comportamiento de algunas variables, con la ayuda de gráficas, y el uso de pairplots, la matriz de correlación de Pearson, entre otros. El desarrollo de este análisis se encuentra en el archivo `EDA.py`. Así mismo, se creó una nube de palabras por medio de la libreria Wordcloud.

# Dashboard

Por medio de la aplicación de Power BI Desktop se construyó un Dashboard, en donde se observa el análisis del dataset una vez hecho el EDA. El desarrollo de este dashboard se encuentra en el archivo AccidentesDashboard.pbix.

# KPIs

En el análisis se tuvieron en cuenta 4 KPIs:

- Tasa de mortalidad total: Tasa de mortalidad a nivel anual, fallecidos en los accidentes aéreos respecto al total de personas en los vuelos involucrados. 

- Tasa de mortalidad promedio por accidente: La tasa de mortalidad promedio por accidente se calculó dividiendo el número total de fallecidos entre el número total de accidentes. 

* Rutas más Peligrosas: Se realizó un análisis de las rutas más peligrosas al contar el número de accidentes por ruta y ordenarlas de manera descendente. 

Tasa de supervivencia:

Sobrevivientes promedio a los accidentes.

Análisis

Se realizón un análisis de los gráficos y datos resultantes al realizar el dashboard en Power Bi, el cual se encuentra en el documento reporte_analisis.docx.

