import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd
from datetime import datetime
from utils.datas_partidas import get_datas_partidas
from utils.times_casa import get_times_casa
from utils.times_fora import get_times_fora
from utils.placares import get_placares, get_placar_time_fora, get_placar_time_casa

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


premier_league = {'nome': 'premier-league',
                  'shortcut': 'GB1',
                  'Header': 'Premier League'}

portugal_a = {'nome': 'liga-nos',
              'shortcut': 'PO1',
              'Header': 'Liga Nos'}

espanha_a = {'nome': 'laliga',
             'shortcut': 'ES1',
             'Header': 'La Liga'}

italia_a = {'nome': 'seria-a',
            'shortcut': 'IT1',
            'Header': 'Serie A Tim'}

alemanha_a = {'nome': 'bundesliga',
              'shortcut': 'L1',
              'Header': 'Bundesliga'}

franca_a = {'nome': 'ligue-1',
            'shortcut': 'FR1',
            'Header': 'Ligue 1'}

brasil_a = {'nome': 'campeonato-brasileiro-seria-a',
            'shortcut': 'BRA1',
            'Header': 'Brasileirão A'}

brasil_b = {'nome': 'campeonato-brasileiro-seria-b',
            'shortcut': 'BRA2',
            'Header': 'Brasileirão B'}

temporadas = [2020, 2019]

ligas = [premier_league, espanha_a, portugal_a, italia_a,
         alemanha_a, franca_a, brasil_a, brasil_b]

nome_ligas = []


link = "https://www.transfermarkt.com.br/premier-league/gesamtspielplan/wettbewerb/GB1/saison_id/2020"

datas = []
timescasa = []
timesfora = []
placar_time_casa = []
placar_time_fora = []

for liga in ligas:
    len_ligas = len(ligas)
    for temporada in temporadas:
        link = f"https://www.transfermarkt.com.br/{liga['nome']}/gesamtspielplan/wettbewerb/{liga['shortcut']}/saison_id/{temporada}"
        print(link)
        # for liga in range(len(ligas)):
        #     for temporada in range(len(temporadas)):
        #         link = f"https://www.transfermarkt.com.br/{liga}/gesamtspielplan/wettbewerb/GB1/saison_id/{temporada}"
        pagina = bs(requests.get(link, headers=headers).content, 'html.parser')
        rodadas = pagina.find_all('div', {'class': 'large-6 columns'})

        # -----------------------
        # Pegando as datas das partidas para todas as rodadas
        datas = datas + get_datas_partidas(rodadas)
        for i in range(len(get_datas_partidas(rodadas))):
            nome_ligas.append(liga['Header'])
        print(len(nome_ligas))
        print(len(datas))
        # -----------------------
        # Pegando times da casa para todas as rodadas

        timescasa = timescasa + get_times_casa(rodadas)

        # -------------------------------

        # Pegando Times Fora de casa para todas as rodadas

        timesfora = timesfora + get_times_fora(rodadas)

        # --------------------------------
        # Pegando Placar de todas as rodadas

        placar = get_placares(rodadas)

        placar_time_casa = placar_time_casa + get_placar_time_casa(placar)
        placar_time_fora = placar_time_fora + get_placar_time_fora(placar)

        # --------------------------------------

df_dict = {'Liga': nome_ligas,
           'Data Partida': datas,
           'Time Casa': timescasa,
           'Gols Time Casa': placar_time_casa,
           'Time Fora': timesfora,
           'Gols Time Fora': placar_time_fora
           }

df = pd.DataFrame.from_dict(df_dict)

df.to_excel(r'C:\Users\bruno\Desktop\dataframe.xlsx', index=False)
