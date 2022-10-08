# O programa irá perguntar o valor da casa o usuário quer comprar, irá perguntar o valor do seu salário, e também em quantos ele quer pagar. O valor da parcela não pode exceder 30% do seu salario
nome = str(input('Qual o seu nome? ')).strip()
print(f'Olá {nome}, estamos felizes em ter o senhor conosco, vamos verificar as propostas do empréstimo.')
casa_v = float(input('Qual o valor da casa: '))
salario = float(input('Qual o valor do seu salário bruto: '))
prazo = int(input('Em até quantos anos você deseja pagar? '))
prestacao = casa_v / (prazo*12)
parcela_minima = salario *30 /100
if prestacao <= parcela_minima:
    print('\033[0;32m A proposta foi aceita\033[m')
    print(f'O valor ser pago mensalmente é de {prestacao:.2f}')
    print('Parábens pela sua conquista') 
else:
    print('\033[0;31mEmprestimo negado. Sentimos muito.\033[m')   
    print(f'O valor da prestação seria de {prestacao:.2f')
    print('Um valor acima de 30% do seu salario')