from time import sleep
from datetime import date
ano = date.today().year
print('-'*10, f'\033[0;33mURNA ELETRONICA\033[0;0m', '-'*10, f'\n           \033[0;033m ELEIÇÕES {ano}\033[0;0m')
secao = int(input('Informe a seção da urna: '))
votantes = int(input('Informe a quantidade de votantes da seção: '))
branco = 0
lula = 0
bolsonaro = 0
simone = 0
ciro = 0
nulo = 0
for i in range(1, votantes+1,1):
    voto = int(input('Qual o seu candidato\n 0 - BRANCO\n 13 - LULA\n 22 - BOLSONARO\n 43 - SIMONE\n 12 - CIRO\n 6 - NULO\n\n'))
    print('O voto está sendo salvo...')
    sleep(2)
    print('\033[0;32m VOTO SALVO\033[0;0m')
    print('\n', '-'*30)
    
    if voto == 0:
        branco += 1
    elif voto == 13:
        lula += 1
    elif voto == 22:
        bolsonaro += 1
    elif voto == 43:
        simone += 1
    elif voto == 12:
        ciro +=1
    elif voto == 6:
        nulo +=1
        
print('Fim da eleição')
print('Será feita a somátoria dos votos')
sleep(2)
print(f'Nessa seção dos {votantes} votos, {branco} foram votos BRANCOS')
print('-'*40)
sleep(1)
print(f'Nessa seção dos {votantes} votos, {lula} foram no candidato do PT LULA')
print('-'*40)
sleep(1)
print(f'Nessa seção dos {votantes} votos, {bolsonaro} foram no candidato do PL BOLSONARO')
print('-'*40)
sleep(1)
print(f'Nessa seção dos {votantes} votos, {simone} foram na candidata do partido aleatorio SIMONE')
print('-'*40)
sleep(1)
print(f'Nessa seção dos {votantes} votos, {ciro} foram no candidato do PDT CIRO')
print('-'*40)
sleep(1)
print(f'Nessa eleição dos {votantes} votos, {nulo} foram nulos.')