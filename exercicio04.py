
# Faça um programa que gera uma lista dos números primos existentes entre 1 e 
# um número inteiro informado pelo usuário. 

# NOT DONE YET !!!
    
num = int(input("\nDigite um número: "))
                                        ########################################################
lista_de_numeros = [2]                    # T A M B É M  T I V E  P R O B L E M A S  N E S S A
                                          # O  V Í D E O  D O  E X E R C Í C I O   - 52 -
                                          # D O  C U R S O  D E  P Y T H O N  D O  G U A N A B A R A
                                          # P O D E  A J U D A R
                                        ########################################################
for numero in range(2, num+1):
    if type(numero/2) == float:
        lista_de_numeros.append(numero)
    
# for numero in lista_de_numeros:
#     if type(numero/2)==int or type(numero/3)==int or type(numero/5)==int or type(numero/5)==int:
#         lista_de_numeros.remove(numero)
        
print(lista_de_numeros)

###################################################################################################################
'''
                                    -  P A R A B É N S ! - 
'''
###################################################################################################################