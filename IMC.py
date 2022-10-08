def imc(peso, altura):
    return peso/(altura*altura)

peso = float(input('informe o seu peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

imc = imc(peso,altura)
print(f'O seu imc é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso'.upper())
elif imc <=25:
    print('peso ideal'.upper())
elif imc<=30:
    print('sobrepeso'.upper())
elif imc <=40:
    print('obesidade'.upper())
else: 
    print('obesidade mórbida'.upper())
    