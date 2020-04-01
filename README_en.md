# covid19_mexico: Processing of the official data for COVID-2019 in Mexico

[ [Español](README.md) | English ]

## Description
The Mexican Ministry of Health (*Secretaría de Salud*) publishes the COVID-19 data as [pfd](/datos/ssalud_pdf/) files. This repo aims to automate the parsing of these documents into [tsv tables](/datos/tablas_originales) to improve data access.

## Data

> Updated: 2020-03-29

The most recent data file from the Secretaría de Salud can be found here:
- [Table in `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.03.29.pdf)
- [Table in `.tsv`](/datos/tablas_originales/20200329_positivos.tsv)

The full table that includes the **dates in which the cases were reported as new** can be found here:
- [Full table in `.tsv`](datos/tablas_procesadas/tabla_completa.tsv)

>For translation of the headers, see [TO_DO](https://github.com/nataquinones/covid19_mexico/blob/master/README_en.md#documentation).

## Data Visualization
### Map
[[ interactive figure](https://plotly.com/~nataquinones/847) |  [table ](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_mapa.tsv)]
<a href="https://plotly.com/~nataquinones/847/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/847.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

### Cumulative cases - Nationwide
[[ interactive figure](https://plotly.com/~nataquinones/849) |  [table ](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_acumulados-nacional.tsv)]
<a href="https://plotly.com/~nataquinones/849/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/849.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

### Cumulative cases - Statewide
> Top 5 states with most cases

[[ interactive figure](https://plotly.com/~nataquinones/854) |  [table ](https://github.com/nataquinones/covid19_mexico/blob/master/datos/tablas_procesadas/20200329_acumulados-estado.tsv)]
<a href="https://plotly.com/~nataquinones/854/" target="_blank" style="display: block; text-align: center;">
  <img src="https://plotly.com/~nataquinones/854.png" style="max-width: 100%;width: 1000px;"  width="1000"/></a>

## Documentation
All the data processing can be found in [`ipynb_notebooks/`](https://github.com/nataquinones/covid19_mexico/tree/master/ipynb_notebooks).

For English speakers:
- I have tried to make the data and code available with Spanish speakers in mind. Nevertheless, I recognize the importance of having this data available in English as well. An extra file translating table headers and directory structure can be found [here](TO_DO). I'm happy to help with other things upon request.

Main things to consider are:
- The first date included in this repo is `2020-03-16`. All cases confirmed before this date are marked as having appeared in `2020-03-15` in the plots and processed data. In the raw data, their date of confirmation is marked as a null value.
- The [full table](datos/tablas_procesadas/tabla_completa.tsv) has a column labeled `pseudo_indice` (*pseudo_index*), which corresponds to the date in which the data point was added as a new case (maked with blue in the `pdf` table), and the index it had on the original table. This has been added because there's no consistent indexing or case ids associated with the data.
- The [processed data](https://github.com/nataquinones/covid19_mexico/tree/master/datos/tablas_procesadas) tables require solving several inconsistencies present in the original data. For this reason, they might differ from what is published by the Mexican Ministry of Health. The decisions I've made regarding what to include or remove can be found in [Issues](https://github.com/nataquinones/covid19_mexico/issues?q=is%3Aissue+is%3Aclosed). If you find any other mayor inconsistency, please let me know and I'll fix it as soon as I can.

## Error reporting
The process to extract the data from the `pdf` files is inconsistent. The files provided by the *Secretaría de Salud* do not have a regular format and that significantly hinders the data extraction. In this repo, I've tried to automate the parsing of the tables, but it is not a perfect script. As confirmed cases increase, it will become harder to manually curate and extract the data, and it is then when having an automated process will pay off. Other efforts have focused on doing manual curation of the data, for that I recommend visiting the following repo: [guzmart/covid19_mex](https://github.com/guzmart/covid19_mex).

If you find any error in my data or bug in my code, I would really appreciate knowing about it, preferably in the form of an [Issue](https://github.com/nataquinones/covid19_mexico/issues), citing the file with the error and a description of the problem.

## Sources
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
