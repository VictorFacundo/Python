soma = 0
for c in range(1,501,2):
    if c % 3 ==0:
        soma = soma+c
        print(c, end=' ')
print(f'\nA soma dos números impares multiplos de 3 é: {soma}')