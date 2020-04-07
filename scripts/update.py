import datetime
import pandas as pd
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
import camelot
import numpy as np

def fecha():
    # user input
    print('Fecha (aaaa-mm-dd):')
    datestr = input()
    
    # parse
    date = datetime.datetime.strptime(datestr, '%Y-%m-%d')
    
    # parse
    return date

def comunicado_tecnico(date, save=False):
    print('Número de casos confirmados:')
    confirmados = input()
    print('Número de casos sospechosos:')
    sospechosos = input()
    print('Número de casos negativos:')
    negativos = input()
    print('Número de defunciones:')
    defunciones = input()
    

    # build dataframe
    df = pd.DataFrame({'status': ['confirmados', 'sospechosos', 'negativos', 'defunciones'],
                       'num': [confirmados, sospechosos, negativos, defunciones],
                       'fecha': [date] * 4})
    
    if save:
        print(df)
        print('¿Guardar en: \'{}\' ? (y/n)'.format(save))
        answer = input()
        if answer is 'y':
            name = '{}_comunicado.tsv'.format(date.strftime('%Y%m%d'))
            df.to_csv('{}/{}'.format(save, name),
                      sep='\t',
                      index=None)
            return df
        else:
            return df


def html_table(df, save=None, current_html=None):
    data = [go.Table(header=dict(values=df['status'].str.title(),
                                 align='center',
                                 fill_color=['rgba(0,0,0,0)'],
                                 line_color=['rgba(0,0,0,0)'],
                                 font=dict(color='#34405B',
                                           size=18)),
                     cells=dict(values=df['num'],
                                fill_color=['rgba(00,0,0,0)'],
                                line_color=['rgba(0,0,0,0)'],
                                align='center',
                                height=40,
                                font=dict(color=['#BF0002',
                                                 '#7F7F7F',
                                                 '#2F5596',
                                                 '#000000'],
                                          size=30)),
                     columnwidth = [1,1,1,1])]
    
    fig = go.Figure(data=data)
    
    fig.update_layout(autosize=True,
                      margin={"r":0,"t":0,"l":0,"b":0},
                      paper_bgcolor='rgba(0,0,0,0)')
    
    if save:
        
        date = df['fecha'][0].strftime('%Y%m%d')
        
        fig.write_html(f'{save}/{date}_tableheader.html',
                       config={'responsive':'true'})
        print(f'Saved in {save}/{date}_tableheader.html')
        
    if current_html:
        fig.write_html(f'{current_html}/CURRENT_tableheader.html',
                       config={'responsive':'true'})
        print (f'Saved in {current_html}/CURRENT_tableheader.html')


def extract_documents(url, outdir='.'):
    '''
    Descarga de documentos de la página de la Secretaría de Salud
    '''
    
    # obtener sitio
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # encotnrar seccion de documentos
    # 2020.03.25: Seccion de documentos bajo <div class="clearfix">
    documents = soup.find('div', attrs={'class': 'clearfix'})
            
    # links de los documentos
    file_urls = []
    
    for href in documents.find_all('a', href=True):
        file_urls.append(href['href'])
        
    # descargar
    for i in range(len(file_urls)):
        file_url = file_urls[i]
        file_name = file_urls[i].split('/')[-1]
        response = requests.get(f'https://www.gob.mx{file_url}')
        
        with open(f'{outdir}/{file_name}', 'wb') as f:
            f.write(response.content)
            print(f'Archivo: {file_name}... descargado.')


def parse_pdf(file, save_name=False, casos_nuevos=False, exception=False):
    '''
    
    '''
    paginas = 'all'
    verify_integrity = True
    header = ['num_caso', 'estado', 'sexo', 'edad', 'fecha_inicio_sintomas', 'id_rt-pcr', 'procedencia', 'fecha_llegada_mx']
    
    if exception:
        if 'pages' in exception.keys():
            paginas = exception['pages']
            
        if 'verify_integrity' in exception.keys():
            verify_integrity = exception['verify_integrity']
        
        if 'header' in exception.keys():
            header = exception['header']

    
    tables = camelot.read_pdf(file, pages=paginas, flavor='stream', row_tol=10)
    print('{} paginas'.format(tables.n))

    # juntar todas las tablas
    tables_list = []
    for i in range(0,tables.n):
        df_i = tables[i].df
        
        # buscar columnas con nan
        df_i= df_i.replace(r'^\s*$', np.nan, regex=True)
        df_i = df_i.replace('NA', np.nan)
        
        # remove na columns
        df_i = df_i.dropna(axis='columns', thresh=10)
        df_i = df_i.T.reset_index(drop=True).T
        
        # quitar filas de titulo
        # por si proceso una pagina vacia
        if len(df_i.columns) != 0:
            df_i[0] = df_i[0].fillna('notnum')
            df_i = df_i[df_i[0].apply(lambda x: x.isnumeric())]
        
            # argregar a lista
            tables_list.append(df_i)

    # juntar tabla unica
    df = pd.concat(tables_list)
    
    
    # renombrar columnas
    df.columns = header
    
    if 'header' in exception.keys():
        
        return df
    
    else:
        # actualizar index
        df.set_index('num_caso', inplace=True, verify_integrity=verify_integrity)
        df.index.name = None

        # convertir a datetime format
        df['fecha_inicio_sintomas'] = pd.to_datetime(df['fecha_inicio_sintomas'], format='%d/%m/%Y')
        df['fecha_llegada_mx'] = pd.to_datetime(df['fecha_llegada_mx'], format='%d/%m/%Y')

        # limpiar nombres de estados
        df['estado'] = df['estado'].str.title()
        df['estado'] = df['estado'].str.replace('Ciudad De México', 'Ciudad de México')
        df['estado'] = df['estado'].str.replace('"Estados \nUnidos"', 'Estados Unidos')

        # CASOS NUEVOS

        if casos_nuevos:
            # interpretar string de casos nuevos
            # by: https://stackoverflow.com/users/190597/unutbu
            # in: https://stackoverflow.com/questions/4726168/parsing-command-line-input-for-numbers
            result = set()

            for part in casos_nuevos.split(','):
                x = part.split('-')
                result.update(range(int(x[0]), int(x[-1]) + 1))

            lista_casos_nuevos = sorted(result)

            # generar lista con anotaciones de casos nuevos
            lista_nuevos = []

            for i in df.index:
                    if int(i) in lista_casos_nuevos:
                        lista_nuevos.append(True)
                    else:
                        lista_nuevos.append(False)

            df['casos_nuevos'] = lista_nuevos

        else:
            print('No se agregara información sobre casos nuevos. (Celdas en azul.)')

        if save_name:
            df.to_csv(f'{save_name}',
                      sep='\t',
                      index=True)

        return df

def update_info(info_path, date, pdf, save_name):
    '''
    '''
    df_info = pd.read_csv(info_path,
                          sep='\t',
                          parse_dates=['fecha'])
    
    if sorted(df_info['fecha'])[-1] != date:
        
        df_info = df_info.append({'fecha': date, 
                                  'pdf_original': pdf,
                                  'archivo_tsv': save_name}, ignore_index=True)
        print(f'Added {date} to table')

        df_info.to_csv(info_path,
                       sep='\t',
                       index=None)
        
        return df_info
    
    else:
        print(f'{date} already in table')
        
        return df_info

