soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 ==0:
        soma = soma + i
        cont = cont+1
        print(i)
print(f'A soma dos termos encontrados é {soma}, e a quantidade de termos encontrados é: {cont}')
            