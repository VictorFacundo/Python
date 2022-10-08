from datetime import date
nome = str(input('Informe o seu nome: ')).strip()
data = int(input('Informe o ano do seu nascimento: '))
ano = date.today().year
idade = ano - data
diferenca_falta = 18-idade
diferenca_mais = idade - 18
if idade<18:
    print(f'Sua idade é {idade} anos')
    print('Você ainda irá se alistar')
    print(f'Ainda falta {diferenca_falta} anos para você se alistar')
elif idade==18:
    print(f'Você tem {idade} anos')
    print('É hora de se alistar')
elif idade>18:
    print(f'Sua idade é {idade} anos')
    print(f'Já passsou da hora de se alistar, {nome}')
    print(f'Já se passou {diferenca_mais} anos do prazo.')
