from random import randint
from time import sleep
Num = randint (1, 100)

esc = input ('Você quer apostar? ')
while True:
    if esc.lower() in ['sim', 's', 'Sim', 'S' ]:
        print ('Que começe o jogo!')
        print ('Um número aleatório será gerado entre 1 a 100')
        sleep (1)
        esc2 = input ('Você acha que ele será maior ou menor que 50? ')
        sleep (1)
        print ('O resultado foi "{}"'.format(Num))
        if esc2.lower() in ['maior']:
            if Num > 50:
                print ('Parabéns, Você ganhou')
            else: print ('Poxa, Você perdeu')
        elif esc2.lower() in ['menor', 'Menor']:
            if Num > 50:
                print ('Poxa, Você perdeu')
            else: print ('Parabéns, Você ganhou')
        else: print ('Escolha inválida')
    elif esc.lower() in ['n', 'não', 'nao']:
        print ('Você escolheu nâo apostar, tenha um bom dia!')
        exit()
    else:
        print ('Escolha inválida.')
    sleep(1)
    esc = input ('Você quer continuar apostando? ')