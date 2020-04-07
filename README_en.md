# covid19_mexico: Processing of the official data for COVID-19 in Mexico

[ [Español](README.md) | English ]

## Visit: [nataquinones.github.io/covid19_mexico/](https://nataquinones.github.io/covid19_mexico/)

## Description
The Mexican Ministry of Health (*Secretaría de Salud*) publishes the COVID-19 data as [pfd](/datos/ssalud_pdf/) files. This repo aims to automate the parsing of these documents into [tsv tables](/datos/tablas_originales) to improve data access.

## Data

> Updated: 2020-04-05

The most recent data file from the Secretaría de Salud can be found here:
- [Table in `pdf`](/datos/ssalud_pdf/Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.04.05.pdf)
- [Table in `.tsv`](/datos/tablas_positivos/20200405_positivos.tsv)

>For translation of the headers, see [here](https://github.com/nataquinones/covid19_mexico/blob/master/README_en.md#documentation).

## Documentation

> I have tried to make the data and code available with Spanish speakers in mind. Nevertheless, I recognize the importance of having this data available in English as well. An extra file translating table headers and directory structure can be found [here](TO_DO). I'm happy to help with other things upon request.

All the data processing can be found in [`ipynb_notebooks/`](https://github.com/nataquinones/covid19_mexico/tree/master/ipynb_notebooks).

## Error reporting
The process to extract the data from the `pdf` files is inconsistent. The files provided by the *Secretaría de Salud* do not have a regular format and that significantly hinders the data extraction. In this repo, I've tried to automate the parsing of the tables, but it is not a perfect script. As confirmed cases increase, it will become harder to manually curate and extract the data, and it is then when having an automated process will pay off. Other efforts have focused on doing manual curation of the data, for that I recommend visiting the following repo: [guzmart/covid19_mex](https://github.com/guzmart/covid19_mex).

If you find any error in my data or bug in my code, I would really appreciate knowing about it, preferably in the form of an [Issue](https://github.com/nataquinones/covid19_mexico/issues), citing the file with the error and a description of the problem.

## Sources
- [Secretaría de Salud: Coronavirus (COVID-19)-Documentos](https://www.gob.mx/salud/documentos/coronavirus-covid-19-comunicado-tecnico-diario-238449)
