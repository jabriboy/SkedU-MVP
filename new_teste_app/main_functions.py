'''
modulo de funções para main do sistema de escalas

author: Gabriel Rocha
'''
from os import system as sys

def dia(day: int) -> None:
    '''
    Seleciona o dia da semana a ser printado

    param:
        day: dia realtivo ao dia da semana
    '''
    if day == 1:
        return '      TERÇA     '
    elif day == 2:
        return '    QUARTA    '
    elif day == 3:
        return '    QUINTA    '
    elif day == 4:
        return '    SEXTA     '
    elif day == 5:
        return '    DOMINGO M   '
    elif day == 6:
        return '  DOMINGO N '

def pos_louvor(pos: int) -> None:
    '''
    Seleciona a posição do louvor

    param:
        pos: posição na matriz da escala
    '''
    if pos == 1:
        return 'VOZ     : '
    elif pos == 2:
        return 'VOZ     : '
    elif pos == 3:
        return 'VOZ-BACK: '
    elif pos == 4:
        return 'VOZ-BACK: '
    elif pos == 5:
        return 'GUITARRA: '
    elif pos == 6:
        return 'TECLADO : '
    elif pos == 7:
        return 'VIOLÃO  : '
    elif pos == 8:
        return 'BAIXO   : '
    elif pos == 9:
        return 'BATERIA : '

def pos_filmagem(pos: int) -> None:
    '''
    Seleciona a posição da filmagem

    param:
        pos: posição na matriz da escala
    '''
    if pos == 1:
        return 'CORTE   : '
    elif pos == 2:
        return 'JOYSTICK: '
    elif pos == 3:
        return 'NOTEBOOK: '
    elif pos == 4:
        return 'CAMERA 4: '

def print_escala(rotation: list, position: int, min: str) -> None:
    '''
    Printa formatado a escala desejada

    params:
        rotation: lista no qual a escala está armazenada
        position: quantidade de posições na escala por dia
        min: nome do ministério da escala
    '''
    print('-'*45, f'{min}', '-'*45, '\n', sep='')
    if position != 1:
        for pos in range(position+1):
            for day in range(7):
                if pos == 0 and day != 0:
                    print(dia(day), end='')
                elif day == 0 and pos == 0:
                    print('    ', end='')
                elif day == 0 and pos != 0:
                    if min == 'LOUVOR':
                        print(pos_louvor(pos), end='')
                    elif min == 'FILMAGEM':
                        print(pos_filmagem(pos), end='')
                
                else:
                    espaco = 14 - len(rotation[pos - 1][day - 1])
                    tam = ' '*espaco
                    print(f'{rotation[pos - 1][day - 1]}', tam, sep='', end='')

            print('\n')
    else:
        for pos in range(position+1):
            for day in range(7):
                if day != 0 and pos == 0:
                    print(dia(day), end='')
                elif day == 0 and pos == 0:
                    print('      ', end='') 
                elif day == 0:
                    print('MESA DE SOM: ', end='')
                
                else:
                    espaco = 14 - len(rotation[day - 1])
                    tam = ' '*espaco
                    print(f'{rotation[day - 1]}', tam, sep='', end='')

            print('\n')
    
    print('-'*100,'\n', sep='')

if __name__ == '__main__':
    sys('cls')
    print(__doc__)