'''
modulo de funções para a geração de escalas do grupo de louvor

author: Gabriel Rocha
'''
from os import system as sys

from .filmagem_function import (
    rotation_filmmaking_1,
    rotation_filmmaking_2, 
    rotation_filmmaking_3, 
    rotation_filmmaking_4
)

from random import choice, shuffle

rotation = [
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', ''],
    ['', '', '', '', '', '']
]

rotation1 = [
    ['', '', '', '', '', ''],  #voz 0
    ['', '', '', '', '', ''],  #back 1
    ['', '', '', '', '', ''],  #back 2
    ['', '', '', '', '', ''],  #back 3
    ['', '', '', '', '', ''],  #guitarra 4
    ['', '', '', '', '', ''],  #teclado 5
    ['', '', '', '', '', ''],  #violão 6
    ['', '', '', '', '', ''],  #baixo 7
    ['', '', '', '', '', '']   #bateria 8
]

rotation2 = [
    ['', '', '', '', '', ''],  #voz 0
    ['', '', '', '', '', ''],  #back 1
    ['', '', '', '', '', ''],  #back 2
    ['', '', '', '', '', ''],  #back 3
    ['', '', '', '', '', ''],  #guitarra 4
    ['', '', '', '', '', ''],  #teclado 5
    ['', '', '', '', '', ''],  #violão 6
    ['', '', '', '', '', ''],  #baixo 7
    ['', '', '', '', '', '']   #bateria 8
]

rotation3 = [
    ['', '', '', '', '', ''],  #voz 0
    ['', '', '', '', '', ''],  #back 1
    ['', '', '', '', '', ''],  #back 2
    ['', '', '', '', '', ''],  #back 3
    ['', '', '', '', '', ''],  #guitarra 4
    ['', '', '', '', '', ''],  #teclado 5
    ['', '', '', '', '', ''],  #violão 6
    ['', '', '', '', '', ''],  #baixo 7
    ['', '', '', '', '', '']   #bateria 8
]

rotation4 = [
    ['', '', '', '', '', ''],  #voz 0
    ['', '', '', '', '', ''],  #back 1
    ['', '', '', '', '', ''],  #back 2
    ['', '', '', '', '', ''],  #back 3
    ['', '', '', '', '', ''],  #guitarra 4
    ['', '', '', '', '', ''],  #teclado 5
    ['', '', '', '', '', ''],  #violão 6
    ['', '', '', '', '', ''],  #baixo 7
    ['', '', '', '', '', '']   #bateria 8
]
week_list = [0, 1, 2, 3]

def get_rotation(list: list) -> bool:
    '''
    gera 4 escalas de semana para o grupo de louvor

    param:
        list: uma lista de dicionário de pessoas do grupo de louvor

    return:
        retorna True caso bem sucedido
    '''
    shuffle(week_list)
    felipe_week = week_list[0]
    wildes_week = week_list[1]

    for week in range(0, 4):
        if week == 0:
            rotation = rotation1
        elif week == 1:
            rotation = rotation2
        elif week == 2:
            rotation = rotation3
        else:
            rotation = rotation4

        for day in range(0, 6):
            day_list = list.copy()

            for pos in range(0, 9):
                while True:
                    if len(day_list) > 0:
                        person_choice = choice(day_list)

                        if day == 0:
                            if pos == 0 or pos == 5:
                                rotation[pos][day] = 'felipe'
                                break
                            else:
                                rotation[pos][day] = ''
                                break

                        elif week == felipe_week and day == 3:
                            if pos == 0 or pos == 5:
                                rotation[pos][day] = 'felipe'
                                break
                            else:
                                rotation[pos][day] = ''
                                break

                        elif week == wildes_week and day == 3:
                            if pos == 0 or pos == 6:
                                rotation[pos][day] = 'wildes'
                                break
                            elif pos == 2 or pos == 3:
                                if validate(person_choice, day, pos, week):
                                    rotation[pos][day] = person_choice['nome']
                                    day_list.remove(person_choice)
                                    break
                            else:
                                rotation[pos][day] = ''
                                break

                        else:
                            if validate(person_choice, day, pos, week):
                                rotation[pos][day] = person_choice['nome']
                                day_list.remove(person_choice)
                                break
                            else:
                                day_list.remove(person_choice)
                    else:
                        day_list = list.copy()
    return True               

def validate(person_choice: dict, day: int, pos: int, week: int):
    '''
    chama todas as funções de validação da escolha de pessoa

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: voz, back, teclado...)
        week: inteiro relacionado a determinada semana do mês

    return:
        retorna True caso todas as funções chamadas retornem True e retorna False caso 1 ou mais retorne False
    '''
    if check_day(person_choice, day) and check_pos(person_choice, pos) and multiple_days(person_choice, day, pos) and check_filmmaking(person_choice, day, week):
            return True
    return False

def check_day(person_choice: dict, day: int):
    '''
    valida se a pessoa escolhida está habilitada para ser escolhida naquele dia

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana

    return:
        retorna True caso a pessoa escolhida possa atuar no dia respectivo da variável day
    '''
    if day == 1:
        if 'wednesday' in person_choice['days']:
            return True
        return False
    elif day == 2:
        if 'thursday' in person_choice['days']:
            return True
        return False
    elif day == 3:
        if 'friday' in person_choice['days']:
            return True
        return False
    elif day == 4:
        if 'sunday_morning' in person_choice['days']:
            return True
        return False
    elif day == 5:
        if 'sunday_evening' in person_choice['days']:
            return True
        return False

def check_pos(person_choice: dict, pos: int):
    '''
    valida se a pessoa escolhida está habilitada para ser escolhida naquela posição

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: voz, back, teclado...)

    return:
        retorna True caso a pessoa escolhida possa atuar na posição respectivo da variável pos
    '''
    if pos == 0 or pos == 1:
        if 'voz' in person_choice['pos']:
            return True
        return False
    elif pos == 2 or pos == 3:
        if 'voz-back' in person_choice['pos']:
            return True
        return False
    elif pos == 4:
        if 'guitarra' in person_choice['pos']:
            return True
        return False
    elif pos == 5:
        if 'teclado' in person_choice['pos']:
            return True
        return False
    elif pos == 6:
        if 'violao' in person_choice['pos']:
            return True
        return False
    elif pos == 7:
        if 'baixo' in person_choice['pos']:
            return True
        return False
    elif pos == 8:
        if 'bateria' in person_choice['pos']:
            return True
        return False

def multiple_days(person_choice: dict, day: int, pos: int):
    '''
    verifica se a pessoa escolhida não ira ficar na escala diversas vezes na semana

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: voz, back, teclado...)

    return:
        retorna True caso a pessoa não tenha passado do limite de vezes na semana e False caso ja tenha passado do limite
    '''
    days = len(person_choice['days'])
    total = days - 3

    for d in range(1, day):
        for p in range(0, pos):
            if person_choice['nome'] == rotation[p][d]:
                total -= 1

                if total <= 0:
                    return False
    
    return True

def check_filmmaking(person_choice: dict, day: int, week: int):
    '''
    verifica a escala da filmagem para que não haja choque das mesmas pessoas no mesmo dia em escalas diferentes

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        week: inteiro relacionado a determinada semana do mês

    return:
        retorna True caso a pessoa escolhida não tenha sido previamente escolhida naquele mesmo dia e semana respectivo na escala da filmagem e False caso ja tenha sido escolhida
    '''
    if week == 0:
        for i in range(0, 4):
            if person_choice['nome'] == rotation_filmmaking_1[i][day]:
                return False
    elif week == 1:
        for i in range(0, 4):
            if person_choice['nome'] == rotation_filmmaking_2[i][day]:
                return False
    elif week == 2:
        for i in range(0, 4):
            if person_choice['nome'] == rotation_filmmaking_3[i][day]:
                return False
    elif week == 3:
        for i in range(0, 4):
            if person_choice['nome'] == rotation_filmmaking_4[i][day]:
                return False

    return True

if __name__ == '__main__':
    sys('cls')
    print(__doc__)
