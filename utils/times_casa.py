def get_times_casa(rodadas):
    timescasa = []
    for item in range(len(rodadas)):
        aux = rodadas[item].find_all(
            'td', {'class': 'text-right no-border-rechts hauptlink'})
        for i in range(len(aux)):
            timescasa.append(aux[i].text)

    for ii in range(len(timescasa)):
        timescasa[ii] = timescasa[ii].replace('\xa0', '')
        timescasa[ii] = timescasa[ii][timescasa[ii].find(')')+1:]
    return timescasa
