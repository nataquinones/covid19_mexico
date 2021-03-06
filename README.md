# covid19_mexico: Procesamiento de los datos oficiales de COVID-19 en México

[ Español | [English](README_en.md) ]

## Visita: [nataquinones.github.io/covid19_mexico/](https://nataquinones.github.io/covid19_mexico/)

## Descripción
La Secretaría de Salud publica la información sobre casos de COVID-19 en México en formato [pdf](/datos/ssalud_pdf/). Este repositorio busca automatizar la conversión de estos documentos para producir [tablas](/datos/tablas_positivos) que faciliten la consulta y el procesamiento de estos datos.

## Datos
El archivo más reciente de la Secretaría de Salud se encuentra aquí:
- [Tabla en `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.04.12.pdf)
- [Tabla en `tsv`](/datos/tablas_positivos/2020012_positivos.tsv)

## Documentación
Todos el procesamiento de datos se encuentra en [`ipynb_notebooks/`](https://github.com/nataquinones/covid19_mexico/tree/master/ipynb_notebooks).
Algunos puntos importantes a considerar son los siguientes:

## Reporte de errores
El proceso de extraer los datos de los archivos `pdf` es inconsistente. Los archivos de la Secretaría de Salud no tienen un formato regular y esto dificulta considerablemente la extración limpia de los datos. En este repositorio, he intentado automatizar la obtención de las tablas, pero no es un algoritmo perfecto. He detectado y corregido errores y estoy constantemente intentando mejorar el script.

Si encuentras algún error en mis datos, te pido me la hagas saber por medio de un [Issue](https://github.com/nataquinones/covid19_mexico/issues) citando el archivo con el problema y una explicación detallada.


## Fuentes
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
- [Directorio de fuentes de datos, repositorios y visualizaciones sobre COVID-19 en México](https://github.com/eduardofv/directorio_covid19_mx)
