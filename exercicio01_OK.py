# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

from time import sleep                                                                  ##########################
                                                                                            # C O L O C A R
ganho_por_hora = float(input('Digite o quanto você recebe por hora!\n'))                    # Try, except aqui !
horas_trabalhadas_mes = int(input('Digite o numéro de horas que você trabalha por mês:\n')) # ^^ ^^ ^^ ^^ ^^ ^^
salario_bruto = ganho_por_hora*horas_trabalhadas_mes                                    ##########################

ir = salario_bruto*11/100               ################        ############        ##############
inss = salario_bruto*8/100    # C O L O C A R  E S P A Ç O  E N T R E  O S  O P E R A D O R E S
sindicato = salario_bruto*5/100         ################        ############        ###############

salario_liquido = salario_bruto-(ir+inss+sindicato) 

print('Hmmmmm, aguarde, calculando dados, hmmmmm....\n')
sleep(1)

print(f'Seu salario bruto é: R${salario_bruto}')
{sleep(0.5)}
print(f'Deste valor foram descontados: ')
{sleep(0.5)}
print(f'Imposto de Renda: R${ir}')
{sleep(0.5)}
print(f'INSS: R${inss}')
{sleep(0.5)}
print(f'Sindicato: R${sindicato}')
{sleep(0.5)}
print(f'Lhe restantando o valor liquido de: R${salario_liquido}')

###################################################################################################################
'''
                                    -  P A R A B É N S ! - 
'''
###################################################################################################################
