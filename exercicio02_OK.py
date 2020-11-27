# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
# em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#     Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from time import sleep
import math

print(f"{' Lojaun dax Tintax ':=^50}\n")

print("""
Nosso estoque hoje:

Latas de tintax 18L por R$80,00 !
Galão de tintax 3,6L por R$25,00 !
""")

lata_pinta_m2 = 108
galao_pinta_m2 = 21.6

area_ser_pintada = float(input('Digite a quantidade de m² a ser pintada:\n'))
litros = area_ser_pintada/6

quantidade_latas = math.ceil(area_ser_pintada/lata_pinta_m2)
quantidade_galoes = math.ceil(area_ser_pintada/galao_pinta_m2)

sleep(0.7)

print(f"""
Caso você deseje comprar em Latas você vai precisar de {quantidade_latas} 
Latas! Gastando R${quantidade_latas*80}!

Caso você deseje comprar em Galão você vai precisar de {quantidade_galoes} Galões! 
Gastando R${quantidade_galoes*25}!

Ou, você pode comprar {litros//18} latas e {math.ceil((litros%18)/3.6)} galões!
Gastando no total R${((litros//18)*80) + (math.ceil((litros%18)/3.6)*25)}
""")