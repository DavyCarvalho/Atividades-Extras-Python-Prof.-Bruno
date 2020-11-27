# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: 
# equilátero, isósceles ou escaleno.

while True:
    try:        
        l1 = float(input("Digite o valor do L1:"))
        l2 = float(input("Digite o valor do L3:"))
        l3 = float(input("Digite o valor do L3:"))
        print('\n')
        
        verificador = True
        
        if l1 == l2 == l3:
            print('Triangulo Equilatero')
            break
        elif l1 == l2 or l1==l3 or l2 == l3:
            print('Triangulo Isósceles')
            break
        else:
            print('Triangulo Escaleno')
            break
            
    except ValueError:
        print('Valor Invalido!\n')
        continue
        