from datetime import date
ano = date.today().year
""" Campeonato nacional de natação, Programa ler a data de nascimento e classifica
em qual campeonato ele irá competir.
sendo  mirim, infantil, junior, sênior, master"""
nasc = int(input('Qual a data de nascimento: '))
idade = ano - nasc

if idade <=9:
    print('mirim'.upper())
elif idade <=14:
    print('infantil'.upper())
elif idade<=19:
    print('junior'.upper())
elif idade <=25:
    print('sênior'.upper())
elif idade > 26:
    print('master'.upper())
    


    
    
    
    