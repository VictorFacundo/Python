soma = 0
for i in range(1,3):
    nota = float(input('Quais suas duas notas: '))
    soma = soma + nota
    media = soma/2    


if media>7:
    print(f'Parábens, você está aprovado. Sua média é {media:.2f}')
elif media>=5.1 and media < 6.9:
    print(f'Você está de recuperação. Sua média é {media:.2f}')
elif media <= 5:
    print(f'Você está reprovado. Sua média é {media:.2f}')

print('\n continue estudando independente do resultado')