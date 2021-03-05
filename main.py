import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd
from datetime import datetime
from utils import corrige_data, corrige_horario, corrige_nome_time, corrige_publico, corrige_resultado, corrige_rodada


class paginas:

    headers = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)

    def retorna_pagina_especifica(self, url):
        return bs(requests.get(url, headers=self.headers).content, 'html.parser')


class pag_tabela_campenatos(paginas):
    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)
        self.url_tab_camp = url_tab_camp
        self.pag_tab_camp = self.retorna_pagina_especifica(self.url_tab_camp)
        self.times_campeonato = self.retorna_ids_times_camp()

    def proc_tag_com_classe_ptc(self, tag, classe):
        return self.pag_tab_camp.find_all(tag, {"class": classe})

    def proc_somente_tag(self, html, tag):
        return html.find_all(tag)

    def retorna_ids_times_camp(self):
        tds = proc_tag_com_classe_ptc(
            'td', 'hauptlink no-border-links show-for-small show-for-pad')
        ids = []
        aux_1 = []
        for i in range(len(tds)):
            aux_1.append(self.proc_somente_tag(tds, 'a')[0]['href'])
        for ii in range(len(aux_1)):
            aux_1[ii] = aux_1[ii][1:]
            aux_2 = aux_1[ii][self.proc_somente_tag(aux_1, 'verein/')+7:]
            ids.append(aux_2[0:self.proc_somente_tag(aux_2, '/')])
        return ids

    def retorna_times_campeonato(self):
        tds = proc_tag_com_classe_ptc(
            'td', 'hauptlink no-border-links show-for-small show-for-pad')
        times = []
        aux_1 = []
        for i in range(len(tds)):
            aux_1.append(self.proc_somente_tag(tds, 'a')[0]['href'])
        for ii in range(len(aux_1)):
            aux_1[ii] = aux_1[ii][1:]
            times.append(aux_1[ii][0:self.proc_somente_tag(aux_1, '/')])
        return times

    def retorna_times_ids(self):
        times_ids = [[], []]
        times = self.retorna_times_campeonato
        ids = self.retorna_ids_times_camp
        for i in range(len(times)):
            times_ids[0].append = times[i]
            times_ids[1].append = ids[i]
        return times_ids


class pag_time(pag_tabela_campenatos):
    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)
        self.


# Get the link to scrap
link_liga = "https://www.transfermarkt.com.br/premier-league/startseite/wettbewerb/GB1/plus/?saison_id=2020"
pagina_liga = bs(requests.get(
    link_liga, headers=headers).content, 'html.parser')

dados_time_campeonato = pagina_liga.find_all(
    'td', {"class": "hauptlink no-border-links show-for-small show-for-pad"})


lista_links_times = []
for i in range(len(dados_time_campeonato)):
    lista_links_times.append(dados_time_campeonato[i].find_all('a')[0]['href'])

nome_times = []
id_times = []
for index in range(len(lista_links_times)):
    lista_links_times[index] = lista_links_times[index][1:]
    nome_times.append(lista_links_times[index]
                      [0:lista_links_times[index].find('/')])
    auxiliar = lista_links_times[index][lista_links_times[index].find(
        'verein/')+7:]
    id_times.append(auxiliar[0:auxiliar.find('/')])

# dados desde o inicio
link_time_full = f"https://www.transfermarkt.com.br/{nome_times[6]}/spielplandatum/verein/{id_times[6]}/plus/1?saison_id=&wettbewerb_id=&day=&heim_gast=&punkte=&datum_von=-&datum_bis=-"

# apenas temporada 20/21
link_time_partial = f"https://www.transfermarkt.com.br/fc-barcelona/spielplandatum/verein/131/plus/1?saison_id=2020&wettbewerb_id=&day=&heim_gast=&punkte=&datum_von=-&datum_bis=-"


# Convert the result
pagina_time = bs(requests.get(link_time_partial,
                              headers=headers).content, 'html.parser')


Partidas = pagina_time.find_all("td", {"class": "no-border-links"})
table_div = pagina_time.find('div', {'class': 'responsive-table'})
table = table_div.find('table')


head_list = []
for th in table.find_all('th'):
    head_list.append(th.text)
head_list.insert(3, 'blank1')
head_list.insert(5, 'blank2')


tbody = table.find('tbody')
trs = tbody.find_all('tr')
dicionario_valores = {}
linhas_tabela = []
lista_auxiliar = []

for ii in range(len(trs)):
    tds = trs[ii].find_all('td')
    lista_auxiliar = []
    dicionario_valores = {}
    for item in range(len(tds)):
        lista_auxiliar.append(tds[item].text)
    for i in range(len(lista_auxiliar)):
        dicionario_valores[head_list[i]] = lista_auxiliar[i]
    linhas_tabela.append(dicionario_valores)


for iii in range(len(linhas_tabela)):
    if len(linhas_tabela[iii].keys()) < 2:
        empty_dict = {}
        for iiii in range(len(head_list)):
            if head_list[iiii] != 'Rodada':
                empty_dict[head_list[iiii]] = ''
            else:

                empty_dict['Rodada'] = corrige_nome_time(
                    linhas_tabela[iii]['Rodada'])
        linhas_tabela[iii] = empty_dict
    else:
        linhas_tabela[iii]['Data'] = corrige_data(linhas_tabela[iii]['Data'])
        linhas_tabela[iii]['Horário'] = corrige_horario(
            linhas_tabela[iii]['Horário'])
        linhas_tabela[iii]['Resultado'] = corrige_resultado(
            linhas_tabela[iii]['Resultado'])
        linhas_tabela[iii]['Rodada'] = corrige_rodada(
            linhas_tabela[iii]['Rodada'])
        linhas_tabela[iii]['Público'] = corrige_publico(
            linhas_tabela[iii]['Público'])
        linhas_tabela[iii]['Time da casa'] = corrige_nome_time(
            linhas_tabela[iii]['Time da casa'])
        linhas_tabela[iii]['Time visitante'] = corrige_nome_time(
            linhas_tabela[iii]['Time visitante'])


# pprint(linhas_tabela)

df = pd.DataFrame(linhas_tabela, columns=head_list)
