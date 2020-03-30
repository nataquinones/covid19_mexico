# covid19_mexico: Processing of the official data for COVID-2019 in Mexico

[ [Español](README.md) | English ]

## Description
TO_DO

## Data

> Updated: 2020-03-29

The most recent data file from the Secretaría de Salud can be found here:
- [Table in `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.03.29.pdf)
- [Table in `.tsv`](/datos/tablas_originales/20200329_positivos.tsv)

The full table that includes the **dates in which the cases were reported as new** can be found here:
- [Full table in `.tsv`](datos/tablas_procesadas/tabla_completa.tsv)

>For translation of the headers and data documentation, [see here](TO_DO).

## Data Visualization
TO_DO

## Documentation
TO_DO

## Error reporting
The process to extract the data from the `pdf` files is inconsistent. The files provided by the *Secretaría de Salud* do not have a regular format and that significantly hinders the data extraction. In this repo, I've tried to automate the parsing of the tables, but it is not a perfect script. As confirmed cases increase, it will become harder to manually curate and extract the data, and it is then when having an automated process will pay off. Other efforts have focused on doing manual curation of the data, for that I recommend visiting the following repo: [guzmart/covid19_mex](https://github.com/guzmart/covid19_mex).

If you find any error in my data or bug in my code, I would really appreciate knowing about it, preferably in the form of an [Issue](https://github.com/nataquinones/covid19_mexico/issues), citing the file with the error and a description of the problem.

## Sources
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
