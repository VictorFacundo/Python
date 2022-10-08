def avista(produto):
    return produto-(produto*10/100)

def avista5(produto):
    return produto-(produto*5/100)

def juros(produto):
    return produto + (produto*20/100)



produto = float(input('Qual o valor do produto: '))
print('=-'*15)
print('Qual a forma de pagamento? ')
forma = int(input(' [1] A VISTA 10% DE DESCONTO \n [2] A VISTA NO CARTÃO 5% DE DESCONTO \n [3] EM ATÉ 2X NO CARTÃO, PREÇO NORMAL \n [4] 3x OU MAIS VEZES NO CARTAO + 20% DE JUROS\n Qual opção deseja?:  '))

if forma ==1:
    compra  = avista(produto)
    print(f'O novo valor do produto é de {compra:.2f}')
elif forma == 2:
    compra = avista5(produto)
    print(f'O novo valor do produto é de {compra:.2f}')
elif forma == 3:
    compra = produto/2
    print(f'O produto foi parcelado em duas vezes no cartão, o valor de cada parcela é {compra:.2f} reais')
elif forma == 4:
    juros = juros(produto)
    parcela = int(input('Deseja parcelar em quantas vezes? '))
    compra = juros/parcela
    print(f'O produto foi parcelado em {parcela} vezes, você pagará {parcela}x de {compra:.2f}')