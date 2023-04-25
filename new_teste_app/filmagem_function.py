'''
modulo de funções para a geração de escalas do grupo de filmagem

author: Gabriel Rocha
'''
from os import system as sys

from random import choice

rotation_filmmaking = [
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
            ]

rotation_filmmaking_1 = [
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
            ]
rotation_filmmaking_2 = [
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
            ]
rotation_filmmaking_3 = [
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
            ]
rotation_filmmaking_4 = [
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', ''],
            ['', '', '', '', '', '']
            ]

def get_filmmaking_rotation(list: list) -> bool:
    '''
    gera 4 escalas de semana para o grupo de filmagem

    param:
        list: uma lista de dicionário de pessoas do grupo de filmagem

    return:
        retorna True caso bem sucedido
    '''
    for week in range(0, 4):
        if week == 0:
            rotation_filmmaking = rotation_filmmaking_1
        elif week == 1:
            rotation_filmmaking = rotation_filmmaking_2
        elif week == 2:
            rotation_filmmaking = rotation_filmmaking_3
        else:
            rotation_filmmaking = rotation_filmmaking_4

        for day in range(0, 6):
            day_list = list.copy()
            for pos in range(0, 4):
                while True:
                    if day == 0 and pos == 3:
                        rotation_filmmaking[pos][day] = '---'
                        break
                    if len(day_list) > 0:
                        people_choice = choice(day_list)
                        day_list.remove(people_choice)
                    else:
                        rotation_filmmaking[pos][day] = '---'
                        break
                    
                    if validate_filmmaking(day, pos, people_choice):
                        rotation_filmmaking[pos][day] = people_choice['name']
                        break
    return True

def validate_filmmaking(day: int, pos: int, people_choice: dict) -> bool:
    '''
    chama todas as funções de validação da escolha de pessoa

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: corte, joystick...)
        week: inteiro relacionado a determinada semana do mês

    return:
        retorna True caso todas as funções chamadas retornem True e retorna False caso 1 ou mais retorne False
    '''
    if days(day, people_choice) == True and positions(pos, people_choice) == True and multiple_days_filmmaking(people_choice) == True and sunday_duplicate(people_choice, day) == True:
        return True
    return False

def days(day: int, people_choice: dict) -> bool:
    '''
    valida se a pessoa escolhida está habilitada para ser escolhida naquele dia

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana

    return:
        retorna True caso a pessoa escolhida possa atuar no dia respectivo da variável day
    '''
    if day == 0:
        if 'tuesday' in people_choice['days_available']:
            return True
    elif day == 1:
        if 'wednesday' in people_choice['days_available']:
            return True
    elif day == 2:
        if 'thursday' in people_choice['days_available']:
            return True
    elif day == 3:
        if 'friday' in people_choice['days_available']:
            return True
    elif day == 4:
        if 'sunday morning' in people_choice['days_available']:
            return True
    else:
        if 'sunday evening' in people_choice['days_available']:
            return True
    return False

def positions(pos: int, people_choice: dict) -> bool:
    '''
    valida se a pessoa escolhida está habilitada para ser escolhida naquela posição

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: voz, back, teclado...)

    return:
        retorna True caso a pessoa escolhida possa atuar na posição respectivo da variável pos
    '''
    if pos == 0:
        if 'switch' in people_choice['pos_capable']:
            return True
    elif pos == 1:
        if 'joystick' in people_choice['pos_capable']:
            return True
    elif pos == 2:
        if 'laptop' in people_choice['pos_capable']:
            return True
    else:
        if 'camera_4' in people_choice['pos_capable']:
            return True
    return False

def multiple_days_filmmaking(people_choice: dict) -> bool:
    '''
    verifica se a pessoa escolhida não ira ficar na escala diversas vezes na semana

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        pos: inteiro relacionado a determinada posição no grupo de louvor (ex: voz, back, teclado...)

    return:
        retorna True caso a pessoa não tenha passado do limite de vezes na semana e False caso ja tenha passado do limite
    '''
    times = len(people_choice['days_available'])
    minus = 0

    for day in range(0, 6):
        for pos in range(0, 4):
            if people_choice['name'] in rotation_filmmaking[pos][day]:
                times =- 1
                minus += 1
                if times == 2 or minus > 2:
                    return False
    
    return True

def sunday_duplicate(people_choice: dict, day: int) -> bool:
    '''
    Quando o dia respectivo do valor da variavel day for domingo a noite, a função verifica se a pessoa escolhida ja foi escolhida para domingo de manhã

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana

    return:
        retorna True caso a pessoa escolhida para domingo a noite não tenha sido escolhida domingo de manhã e False caso ja tenha sido escolhida para domingo de manhã
    '''
    if day == 5:
        for pos in range(0, 4):
            if people_choice['name'] in rotation_filmmaking[pos][4]:
                return False
    
    return True

if __name__ == '__main__':
    sys('cls')
    print(__doc__)
