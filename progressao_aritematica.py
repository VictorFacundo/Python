primeiro = int(input('Qual o primeiro termo?: '))
razao = int(input('Qual a razão: '))
termo = primeiro + (10-1)*razao
for i in range(primeiro, termo, razao):
    print(i, end='->')
