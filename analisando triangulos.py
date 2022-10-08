"""Informe os 3 segmentos do triangulo, para verificar se equilátero, isosceles, escaleno"""
s1 = float(input('primeiro segmento: '))
s2 = float(input('seguno segmento: '))
s3 = float(input('terceiro segmento: '))

if s1==s2==s3:
    print('Triangulo equilátero'.upper())
if s1!=s2!=s3!=s1:
    print('Triangulo escaleno'.upper())
else:
    print('Isoceles'.upper())
        