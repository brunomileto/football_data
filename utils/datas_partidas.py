
import datetime


def get_datas_partidas(rodadas):
    datas = []
    for item in range(len(rodadas)):
        aux = rodadas[item].find_all('td', {'class': 'hide-for-small'})
        for i in range(len(aux)):
            datas.append(aux[i].text)
    ddatas = [[], []]
    for item in range(len(datas)):
        datas[item] = datas[item].replace('\n', '')
        datas[item] = datas[item].replace('\t', '')
        datas[item] = datas[item].replace(' ', '')
        datas[item] = datas[item].replace('sáb', '')
        datas[item] = datas[item].replace('dom', '')
        datas[item] = datas[item].replace('seg', '')
        datas[item] = datas[item].replace('ter', '')
        datas[item] = datas[item].replace('qua', '')
        datas[item] = datas[item].replace('qui', '')
        datas[item] = datas[item].replace('sex', '')

        if ((item == 0) or (item % 2 == 0)):
            ddatas[0].append(datas[item])
        else:
            ddatas[1].append(datas[item])

    datas = []
    for item in range(len(ddatas[0])):
        datas.append(ddatas[0][item])

    for iii in range(len(datas)):
        if datas[iii] == '':
            datas[iii] = datas[iii-1]

    for iiii in range(len(datas)):
        datas[iiii] = datetime.datetime.strptime(
            datas[iiii], '%d/%m/%y').date()

    return datas
