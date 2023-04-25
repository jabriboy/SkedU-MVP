from .filmagem_function import (
    get_filmmaking_rotation,
    rotation_filmmaking_1,
    rotation_filmmaking_2,
    rotation_filmmaking_3,
    rotation_filmmaking_4
    )
from .person_filmagem import list_filmmaking
from .louvor_functions import (
    get_rotation,
    rotation1, 
    rotation2, 
    rotation3, 
    rotation4
)
from .person_louvor import list
from .mixagem_functions import (
    get_rotation_mixagem,
    rotation_mixagem_1,
    rotation_mixagem_2,
    rotation_mixagem_3,
    rotation_mixagem_4
)
from .person_mixagem import list_mixagem

from .main_functions import *
from os import system as sys

# while True:
#     if get_filmmaking_rotation(list_filmmaking) and get_rotation(list) and get_rotation_mixagem(list_mixagem):
#         break

# for i in range(4):
#     if i == 0:
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_filmmaking_1, 4, 'FILMAGEM')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation1, 9, 'LOUVOR')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_mixagem_1, 1, 'MIXAGEM')
#         continuar = input('--->')

#     elif i == 1:
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_filmmaking_2, 4, 'FILMAGEM')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation2, 9, 'LOUVOR')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_mixagem_2, 1, 'MIXAGEM')
#         continuar = input('--->')

#     elif i == 2:
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_filmmaking_3, 4, 'FILMAGEM')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation3, 9, 'LOUVOR')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_mixagem_3, 1, 'MIXAGEM')
#         continuar = input('--->')
        
#     elif i == 3:
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_filmmaking_4, 4, 'FILMAGEM')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation4, 9, 'LOUVOR')
#         continuar = input('--->')
#         sys('cls')
#         print(f'SEMANA {i+1}')
#         print_escala(rotation_mixagem_4, 1, 'MIXAGEM')
#         continuar = input('--->')
