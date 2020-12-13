frase = ('  curso em video python  ')
print(frase)
# Se inserir cochetes e um numero da ordem saira a letra referente a ordem do caractere, como visto abaixo
print(frase[4])
# Se inserir entre os cochetes [1:13] sera considerado o 1 numero ate o decimo terceiro caractere, como visto no exemplo
print(frase[2:5])
# Se inserir entre os conhetes um numero sem o inicial ou final sera considerado do inicio ou fim, como visto abaixo
print(frase[:15])
# Se inserir entre os cochetes mais um : e outro numero sera considerado a quatidade de pulo de caracteres
print(frase[1:9:2])
# Para texto longo podese utilizar print(""" texto longo""") para inserir o texto de uma vez
print("""Python é uma linguagem de programação de alto nível, interpretada, de script,
         imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte.
         Foi lançada por Guido van Rossum em 1991""")
# A função len(print()) e usada para contar os caracteres da frase
print(len(frase))
# A função strip() remove os espaços inuteis da frase
print((frase.strip()))
# A função replace troca uma palavra por outra independente da quantidade de caracteres
print(frase.replace('python','Android'))
# Função in diz com true e false se palavra ou caractere esta na frase
print('curso' in frase)
# Função frase diz em que posição a palavra se inicia, se nao existir ira aparecer -1
print(frase.find('video'))
# A funçao split divide a frase em palavras colocando a mesma em uma lista
print(frase.split())

