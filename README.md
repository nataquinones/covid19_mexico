# covid19_mexico: Procesamiento de los datos oficiales de COVID-2019 en México

[ Español | [English](README_en.md) ]

## Descripción
La Secretaría de Salud publica la información sobre casos de COVID-2019 en México en formato [pdf](/datos/ssalud_pdf/). Este repositorio busca automatizar la conversión de estos documentos para producir [tablas](/datos/tablas_originales) que faciliten la consulta y el procesamiento de estos datos.

## Datos

> Última actualización: 2020-03-29

El archivo más reciente de la Secretaría de Salud se encuentra aquí:
- [Tabla en `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.03.29.pdf)
- [Tabla en `tsv`](/datos/tablas_originales/20200329_positivos.tsv)

La tabla completa que incluye las **fechas en las que el caso fue reportado como nuevo** se encuentra aquí:
- [Tabla completa en `tsv`](datos/tablas_procesadas/tabla_completa.tsv)

## Visualización
### Mapa
[[versión dinámica](https://plotly.com/~nataquinones/847) |  [tabla](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_mapa.tsv)]
<a href="https://plotly.com/~nataquinones/847/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/847.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

### Acumulado de casos nacionales
[[versión dinámica](https://plotly.com/~nataquinones/849) |  [tabla](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_acumulados-nacional.tsv)]
<a href="https://plotly.com/~nataquinones/849/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/849.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

### Acumulado por estados
> Los 5 con mayor número de casos

[[versión dinámica](https://plotly.com/~nataquinones/854) |  [tabla](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_acumulados-estado.tsv)]
<a href="https://plotly.com/~nataquinones/854/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/854.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

## Documentación
Todos el procesamiento de datos se encuentra en [`ipynb_notebooks/`](https://github.com/nataquinones/covid19_mexico/tree/master/ipynb_notebooks).
Algunos puntos importantes a considerar son los siguientes:
- El primer archivo pdf que se procesa es del día `2020-03-16`, todos los casos anteriores a este día se marcan como `2020-03-15`.
- La [tabla completa](datos/tablas_procesadas/tabla_completa.tsv) tiene una columna llamada `pseudo_indice` que corresponde a la fecha en la que el dato fue agregado como nuevo y el indice en la tabla original.
- Los [datos procesados](https://github.com/nataquinones/covid19_mexico/tree/master/datos/tablas_procesadas) requieren resolver ciertas inconsistencias presentes en los datos originales. Las decisiones que han tomado para consolidar estos datos se pueden encontrar en el historial de [Issues](https://github.com/nataquinones/covid19_mexico/issues?q=is%3Aissue+is%3Aclosed), donde documento cualquier información sobre cambios en los datos. Por lo mismo, pueden diferir ligeramente de lo publicado por la Secretaría de Salud. Si encuentras inconsistencias mayores, házmelo saber.

## Reporte de errores
El proceso de extraer los datos de los archivos `pdf` es inconsistente. Los archivos de la Secretaría de Salud no tienen un formato regular y esto dificulta considerablemente la extración limpia de los datos. En este repositorio, he intentado automatizar la obtención de las tablas, pero no es un algoritmo perfecto. He detectado y corregido errores y estoy constantemente intentando mejorar el script. Conforme los casos aumenten, será más complicado hacer una curaduría manual, y es donde la automatización de la descarga de la información valdrá la pena. Otros esfuerzos han hecho un gran trabajo para limpiar y resolver conflictos de datos, recomiendo visitar el repositorio de [guzmart/covid19_mex](https://github.com/guzmart/covid19_mex) para obtener los datos con curaduría manual.

Si encuentras algún error en mis datos, te pido me la hagas saber por medio de un [Issue](https://github.com/nataquinones/covid19_mexico/issues) citando el archivo con el problema y una explicación detallada.


## Fuentes
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
