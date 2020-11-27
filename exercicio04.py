
# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

    
num = int(input("\nDigite um número: "))

lista_de_numeros = [2]

for numero in range(2, num+1):
    if type(numero/2) == float:
        lista_de_numeros.append(numero)
    
# for numero in lista_de_numeros:
#     if type(numero/2)==int or type(numero/3)==int or type(numero/5)==int or type(numero/5)==int:
#         lista_de_numeros.remove(numero)
        
print(lista_de_numeros)
    