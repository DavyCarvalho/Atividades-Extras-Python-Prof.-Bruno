# Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para 
# gerar numeros aleatórios, simulando os lançamentos dos dados.

# COPIADO DA NET E TENTANDO ENTENDER O QUE ESTÁ ACONTECENDO AQUI !!!

import random
                                                        ########################################
                                                #  Eu também usei a biblioteca random, a função randint
                                                #  também usei o append mesmo, e fiz um "count" toda vez que
                                                # Reiniciava o loop, boa competênciaa!!!  :)
                                                        ########################################
dado = [0]*6

for i in range(0,100):
    lancamento = random.randint(0,5)
    dado[lancamento] += 1                                #######################################
    # dado.append(lancamento) qual a diferença  ?????   #  E L E  S ´O  A D I C I O N O U
                                                        #  C O M O  F A Z E M O S  E M  A D I Ç Ã O
                                                        #  D E  L I S T A
                                                         #######################################
print(dado)    

for i in range(0, 6):
    print('%d - %d' %  (i+1, dado[i]))

###################################################################################################################
'''
                                    -  P A R A B É N S ! - 
'''
###################################################################################################################