print('-'*50)
n = int(input('Informe a quantidade de termos? '))
print('-'*50)
n1=0
n2=1 
print('\n')
print(f' {n1}\n {n2}')
contador =3 
while contador <=n:
    n3=n1+n2
    print(end='')
    print(f' {n3}')
    n1=n2
    n2=n3
    contador +=1 
print('Fim')
    



