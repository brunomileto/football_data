def get_times_fora(rodadas):
    timesfora = []
    for item in range(len(rodadas)):
        aux = rodadas[item].find_all(
            'td', {'class': 'no-border-links hauptlink'})
        for i in range(len(aux)):
            timesfora.append(aux[i].text)

    for ii in range(len(timesfora)):
        timesfora[ii] = timesfora[ii].replace('\xa0', '')
        if timesfora[ii].find('(') > 0:
            timesfora[ii] = timesfora[ii][:timesfora[ii].find('(')]
    return timesfora
