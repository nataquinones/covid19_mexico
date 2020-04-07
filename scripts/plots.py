import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go
import os
import numpy as np


def parse_generales(dir_path):
    
    all_dfs = []
    for file in os.listdir(dir_path):
        if file.endswith('_comunicado.tsv'):
            table_path = os.path.join(dir_path, file)
            df = pd.read_csv(table_path,
                             sep='\t',
                             index_col=None,
                             parse_dates=['fecha'])
            all_dfs.append(df)
    
    df_m = pd.concat(all_dfs)
    
    df_m = df_m.sort_values('fecha')
    
    df_m = df_m.reset_index(drop=True)
    
    return df_m


def plot_cofirmados(dir_path, save=None, current_html=None):
    
    df = parse_generales(dir_path)
    
    df_confirmados = df[df['status'] == 'confirmados'].copy()
    
    sorted_dates = sorted(df_confirmados['fecha'])
    range_start = sorted_dates[0] - datetime.timedelta(hours=10)
    range_end = sorted_dates[-1] + datetime.timedelta(hours=10)
    
    fig = px.scatter(df_confirmados, x="fecha", y="num")
    
    fig.data[0].update(mode='markers+lines',
                       marker=dict(color='rgb(255, 0, 0)',
                                   size=4),
                       hovertemplate='<i>%{x|%Y-%m-%d}</i><br><b>%{y}</b>',
                       line=dict(width=1))
    
    fig.update_layout(title={'text': '<b>covid19</b>: casos confirmados <i>{}</i>'.format(sorted_dates[-1].strftime('%Y-%m-%d')),
                             'x': 0.03,
                             'y': 0.02},
                      width=900,
                      height=500,
                      margin={"r":30,"t":30,"l":50,"b":90},
                      autosize=False,
                      plot_bgcolor='rgb(243, 243, 243)',
                      xaxis=dict(showline=True,
                                 title=None,
                                 showgrid=False,
                                 range=[range_start, range_end],
                                 linewidth=2,
                                 type='date',
                                 dtick='2000-01-01',
                                 tickformat='%m-%d',
                                 ticks='inside',
                                 ticklen=5),
                      yaxis=dict(autorange=True,
                                 title=None))
    
    if save:
        
        date = sorted_dates[-1].strftime('%Y%m%d')
        
        fig.write_html(f'{save}/{date}_casosconfirmados-nacional.html',
                       config={'responsive':'true'})
        print(f'Saved in {save}/{date}_casosconfirmados-nacional.html')
        
    if current_html:
        fig.write_html(f'{current_html}/CURRENT_casosconfirmados-nacional.html',
                       config={'responsive':'true'})
        print (f'Saved in {current_html}/CURRENT_casosconfirmados-nacional.html')

        
    return fig.show()


def plot_map(file, date, save=None, current_html=None):
    
    file_estados = '../misc/coord_estados_mexico.tsv'
    
    df = pd.read_csv(file,
                     sep='\t',
                     index_col=0,
                     parse_dates=['fecha_inicio_sintomas', 'fecha_llegada_mx'])
    
    df_estados = pd.read_csv(file_estados,
                             sep='\t')
    
    estados_counts = df['estado'].value_counts()
    estados_counts = estados_counts.reset_index()
    estados_counts.columns = ['estado', 'num']

    df_m = df_estados.merge(estados_counts, how='left')
    df_m['log_count'] = np.log(df_m['num'])
    df_m['num'] = df_m['num'].fillna(0).astype(int)
    df_m['log_count'] = df_m['log_count'].fillna(0)
    
    # Map
    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lon = df_m['long'],
        lat = df_m['lat'],
        mode = 'markers',
        hoverinfo = 'text',
        text = df_m['abrev'] + '<br>' + df_m['num'].astype(str),
        marker = dict(
            size = df_m['log_count'],
            color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)')
        )))

    fig.update_layout(showlegend = False,
                      margin={"r":0,"t":0,"l":0,"b":0},
                      paper_bgcolor='rgba(0,0,0,0)',
                      geo = dict(scope = 'world',
                                 projection_type = 'natural earth',
                                 showcountries = True,
                                 landcolor = 'rgb(243, 243, 243)',
                                 countrycolor = 'rgb(204, 204, 204)',
                                 lataxis_range=[14,34],
                                 lonaxis_range=[-127, -76]))
    
    if save:
        datestr = date.strftime('%Y%m%d')
        
        fig.write_html(f'{save}/{datestr}_mapa-confirmados.html',
                       config={'responsive':'true'})
        print(f'Saved in {save}/{datestr}_mapa-confirmados.html')
        
    if current_html:
        fig.write_html(f'{current_html}/CURRENT_mapa-confirmados.html',
                       config={'responsive':'true'})
        print (f'Saved in {current_html}/CURRENT_mapa-confirmados.html')

    return fig.show()

