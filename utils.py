
def corrige_publico(publico):
    publico = publico.strip()
    if publico == 'x':
        publico = ''
    return publico


def corrige_nome_time(nome_time):
    nome_time = nome_time.replace('\xa0', '')
    nome_time = nome_time.replace('\n', '')
    nome_time = nome_time.replace('\t', '')
    nome_time = nome_time.strip()
    if nome_time.find('(') > 0:
        nome_time = nome_time[:nome_time.find('(')]
    return nome_time


def corrige_data(data):
    data = data[data.find(' ')+1:]
    data = data.strip()
    data = data.replace('.', '/')
    return data


def corrige_horario(horario):
    horario = horario.replace('\n', '')
    horario = horario.strip()
    if horario == 'desconhecido':
        horario = ''
    return horario


def corrige_resultado(resultado):
    resultado = resultado.strip()
    if resultado == '-:-':
        resultado = ''
    return resultado


def corrige_rodada(rodada):
    rodada = rodada.replace('\n', '')
    rodada = rodada.replace('\t', '')
    rodada = rodada.strip()
    return rodada
