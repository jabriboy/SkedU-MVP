'''
modulo de funções para a geração de escalas do grupo de mixagem

author: Gabriel Rocha
'''
from os import system as sys

from .louvor_functions import (
    rotation_filmmaking_1,
    rotation_filmmaking_2,
    rotation_filmmaking_3,
    rotation_filmmaking_4,
    rotation1,
    rotation2,
    rotation3,
    rotation4
)

from random import choice

rotation_mixagem = ['', '', '', '', '', '']

rotation_mixagem_1 = ['', '', '', '', '', '']
rotation_mixagem_2 = ['', '', '', '', '', '']
rotation_mixagem_3 = ['', '', '', '', '', '']
rotation_mixagem_4 = ['', '', '', '', '', '']



def get_rotation_mixagem(list: list):
    '''
    gera 4 escalas de semana para o grupo de mixagem

    param:
        list: uma lista de dicionário de pessoas do grupo de mixagem

    return:
        retorna True caso bem sucedido
    '''
    week_list = []
    for i in list:
        week_list.append(i)
    
    for week in range(0, 4):
        if week == 0:
            rotation_mixagem = rotation_mixagem_1
        elif week == 1:
            rotation_mixagem = rotation_mixagem_2
        elif week == 2:
            rotation_mixagem = rotation_mixagem_3
        else:
            rotation_mixagem = rotation_mixagem_4
        
        for day in range(0, 6):
            qnt_ciclos = 0
            times = 0
            while True:
                if len(week_list) > 0:
                    person_choice = choice(week_list)
                    qnt_ciclos += 1

                    if day == 0:
                        rotation_mixagem[day] = 'luan'
                        break
                    
                    if validate(person_choice, day, week):
                        rotation_mixagem[day] = person_choice['name']
                        week_list.remove(person_choice)
                        break

                    elif qnt_ciclos > len(week_list) + 1:
                        if times < 2:
                            qnt_ciclos = 0
                            week_list = list.copy()
                        else:
                            rotation_mixagem[day] = 'EXTRA'
                            break
                        times += 1 

    return True        

def validate(person_choice: dict, day: int, week: int):
    '''
    chama todas as funções de validação da escolha de pessoa

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        week: inteiro relacionado a determinada semana do mês

    return:
        retorna True caso todas as funções chamadas retornem True e retorna False caso 1 ou mais retorne False
    '''
    if check_day(person_choice, day) and check_filmmaking(person_choice, day, week) and check_worship(person_choice, day, week):
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
    if day == 0:
        if 'tuesday' in person_choice['days']:
            return True
        return False
    elif day == 1:
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
        if 'sunday morning' in person_choice['days']:
            return True
        return False
    else:
        if 'sunday evening' in person_choice['days']:
            return True
        return False

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
            if person_choice['name'] == rotation_filmmaking_1[i][day]:
                return False
    elif week == 1:
        for i in range(0, 4):
            if person_choice['name'] == rotation_filmmaking_2[i][day]:
                return False
    elif week == 2:
        for i in range(0, 4):
            if person_choice['name'] == rotation_filmmaking_3[i][day]:
                return False
    elif week == 3:
        for i in range(0, 4):
            if person_choice['name'] == rotation_filmmaking_4[i][day]:
                return False

    return True

def check_worship(person_choice: dict, day: int, week: int):
    '''
    verifica a escala do louvor para que não haja choque das mesmas pessoas no mesmo dia em escalas diferentes

    params:
        person_choice: dicionário da pessoa escolhida com nome e restrições de dia e posição
        day: inteiro respectivo a determinado dia da semana
        week: inteiro relacionado a determinada semana do mês

    return:
        retorna True caso a pessoa escolhida não tenha sido previamente escolhida naquele mesmo dia e semana respectivo na escala do louvor e False caso ja tenha sido escolhida
    '''
    if week == 0:
        for i in range(0, 9):
            if person_choice['name'] == rotation1[i][day]:
                return False
    elif week == 1:
        for i in range(0, 9):
            if person_choice['name'] == rotation2[i][day]:
                return False
    elif week == 2:
        for i in range(0, 9):
            if person_choice['name'] == rotation3[i][day]:
                return False
    elif week == 3:
        for i in range(0, 9):
            if person_choice['name'] == rotation4[i][day]:
                return False

    return True

if __name__ == '__main__':
    sys('cls')
    print(__doc__)