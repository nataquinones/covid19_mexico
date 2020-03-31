# covid19_mexico: Procesamiento de los datos oficiales de COVID-2019 en México

[ Español | [English](README_en.md) ]

## Descripción
TO_DO

## Datos

> Última actualización: 2020-03-29

El archivo más reciente de la Secretaría de Salud  se encuentra aquí:
- [Tabla en `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.03.29.pdf)
- [Tabla en `.tsv`](/datos/tablas_originales/20200329_positivos.tsv)

La tabla completa que incluye las **fechas en las que el caso fue reportado como nuevo** se encuentra aquí:
- [Tabla completa en `.tsv`](datos/tablas_procesadas/tabla_completa.tsv)

## Visualización

<a href="https://plotly.com/~nataquinones/849/?share_key=NQs6mraaw1EHZVVbALZHTj" target="_blank" title="20200329_growth" style="display: block; text-align: center;"><img src="https://plotly.com/~nataquinones/849.png?share_key=NQs6mraaw1EHZVVbALZHTj" alt="20200329_growth" style="max-width: 100%;width: 1000px;"  width="1000" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>

<a href="https://plotly.com/~nataquinones/847/?share_key=2Yu1MznsRh1mokhgGft5HU" target="_blank" title="20200329_staticmap" style="display: block; text-align: center;"><img src="https://plotly.com/~nataquinones/847.png?share_key=2Yu1MznsRh1mokhgGft5HU" alt="20200329_staticmap" style="max-width: 100%;width: 1000px;"  width="1000" onerror="this.onerror=null;this.src='https://plotly.com/404.png';" /></a>




## Documentación
TO_DO

## Reporte de errores
El proceso de extraer los datos de los archivos `pdf` es inconsistente. Los archivos de la Secretaría de Salud no tienen un formato regular y esto dificulta considerablemente la extración limpia de los datos. En este repositorio, he intentado automatizar la obtención de las tablas, pero no es un algoritmo perfecto. He detectado y corregido errores y estoy constantemente intentando mejorar el script. Conforme los casos aumenten, será más complicado hacer una curaduría manual, y es donde la automatización de la descarga de la información valdrá la pena. Otros esfuerzos han hecho un gran trabajo para limpiar y resolver conflictos de datos, recomiendo visitar el repositorio de [guzmart/covid19_mex](https://github.com/guzmart/covid19_mex) para obtener los datos con curaduría manual.

Si encuentras algún error en mis datos, te pido me la hagas saber por medio de un [Issue](https://github.com/nataquinones/covid19_mexico/issues) citando el archivo con el problema y una explicación detallada.


## Fuentes
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
