# Conta espaços e vogais. Dado uma string com uma frase 
# informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.


frase = input('Digite uma frase com espaços:\n\n').lower()

print(f"""
      A frase tem:
      {frase.count(" ")} espaços
      {frase.count("a")} letras A
      {frase.count("e")} letras E
      {frase.count("i")} letras I
      {frase.count("o")} letras O
      {frase.count("u")} letras U
      """)
