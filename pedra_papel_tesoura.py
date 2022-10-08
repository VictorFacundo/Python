from time import sleep
from random import choice
print('=-'*20)
print(   'PEDRA - PAPEL - TESOURA'  )
print(' Você tem que vencer o computador no jogo de pedra, papel e tesoura')
opcao = str(input('Qual sua opçao?\n papel \n pedra \n tesoura\n ')).strip()
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
print('=-=-'*15)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('E')
sleep(1)
print('TESOURA')
print('=-=-'*15)

if opcao == 'pedra' and pc == 'tesoura':
    print(f'Você venceu. Eu escolhi {pc}, e você {opcao}')
elif opcao == 'pedra' and pc == 'pedra':
    print(f'A gente deu empate, nós dois colocamos {pc}')
elif opcao == 'pedra' and pc == 'papel':
    print(f'Você perdeu. Você escolheu {opcao} e eu {pc}')
elif opcao == 'papel' and pc == 'tesoura':
    print(f'Você perdeu. Eu coloquei {pc} e você {opcao}')
elif opcao == 'papel' and pc == 'papel':
    print(f'A gente deu empate, nós colocamos {pc}')
elif opcao == 'papel' and pc == 'pedra':
    print(f'Você venceu, eu coloquei {pc} e você {opcao}')
elif opcao == 'tesoura' and pc == 'tesoura':
    print(f'A gente deu empate, nós dois colocamos {pc}')
elif opcao == 'tesoura' and pc == 'papel':
    print(f'Você venceu. Eu coloquei {pc} e você {opcao}')
elif opcao == 'tesoura' and pc == 'pedra':
    print(f'Você perdeu. Eu coloquei {pc} e você {opcao}')
print('Fim de jogo')
