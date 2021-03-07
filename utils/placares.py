def get_placares(rodadas):
    placar = []
    for item in range(len(rodadas)):
        aux = rodadas[item].find_all(
            'td', {'class': 'zentriert hauptlink'})
        for i in range(len(aux)):
            placar.append(aux[i].text)
    return placar


def get_placar_time_casa(placar):
    placar_time_casa = []
    for ii in range(len(placar)):
        placar[ii] = placar[ii].replace('\xa0', '')
        placar_time_casa.append(placar[ii][:placar[ii].find(':')])

    for i in range(len(placar_time_casa)):
        if placar_time_casa[i] != '-':
            placar_time_casa[i] = int(placar_time_casa[i])
    return placar_time_casa


def get_placar_time_fora(placar):
    placar_time_fora = []
    for ii in range(len(placar)):
        placar[ii] = placar[ii].replace('\xa0', '')
        placar_time_fora.append(placar[ii][placar[ii].find(':')+1:])

    for i in range(len(placar_time_fora)):
        if placar_time_fora[i] != '-':
            placar_time_fora[i] = int(placar_time_fora[i])

    return placar_time_fora
