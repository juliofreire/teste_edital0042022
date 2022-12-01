# Há 9 bolinhas de metal, todas iguais visualmente. 8 delas têm o mesmo peso e 1 é mais pesada.
# Qual é a bolinha mais pesada?
# Você tem uma balança (daquelas antigas com 2 pratos) e 2 tentativas de pesagem para descobrir
# qual é a bolinha mais pesada.

# Para esse problema, primeiramente foi pensado uma maneira de resolver o problema da pesagem.

# Resolução:
# Ele foi pensado da seguinte forma, divide-se as 9 bolinhas em grupos de 3. Faz-se a pesagem de
# 3 bolinhas em um prato e 3 em outro, caso os pesos dêem iguais, é possível afirmar que a bolinha
# mais pesada está no grupo que não foi pesado e caso dê diferente, basta pegar as 3 bolinhas que
# tiveram mais peso. Em mãos das 3 mais pesadas, basta agora efetuar a pesagem de duas delas, uma
# em cada balança e obter conclusões análogas a da primeira pesagem para chegar a resposta.

import numpy as np

# condições iniciais do problema
n_bolinhas = 9
num_bolinhas = np.arange(n_bolinhas)

# peso das bolinhas gerado aleatoriamente
peso_padrao = 100 # numero mágico qualquer
peso_bolinhas = peso_padrao * np.ones([n_bolinhas])

# adicionado peso a mais em uma das bolinhas, aleatoriamente
n_rand = np.random.randint(n_bolinhas)
peso_bolinhas[n_rand] += 1

print("As bolinhas foram embaralhadas na seguinte ordem: " + str(num_bolinhas) + "\n")

# separação em 3 grupos
grupo_1 = num_bolinhas[0:3]
grupo_2 = num_bolinhas[3:6]
grupo_3 = num_bolinhas[6:9]

# pesagem de dois grupos de bolinhas
peso_g1 = np.sum(peso_bolinhas[grupo_1])
peso_g2 = np.sum(peso_bolinhas[grupo_2])

# comparação dos grupos de bolinhas (papel da balança)
# seleção do grupo de bolinhas mais pesado
print("Realizando a primeira pesagem e comparação...\n")

if (peso_g1 > peso_g2):
    grupo_mais_pesado = grupo_1
elif (peso_g2 > peso_g1):
    grupo_mais_pesado = grupo_2
else: # (peso_g1 == peso_g2)
    grupo_mais_pesado = grupo_3
print(f'O grupo mais pesado é formado pelas bolinhas: {grupo_mais_pesado} \n')

##### SEGUNDA PESAGEM

# divisão em 3 grupos menores
bolinha_1 = grupo_mais_pesado[0]
bolinha_2 = grupo_mais_pesado[1]
bolinha_3 = grupo_mais_pesado[2]

# pesagem de 2 grupos de bolinhas
peso_bolinha_1 = peso_bolinhas[bolinha_1]
peso_bolinha_2 = peso_bolinhas[bolinha_2]

# comparação dos pesos do grupo menor
# seleção da bolinha mais pesada
print("Realizando a segunda pesagem e comparação...\n")

if (peso_bolinha_1 > peso_bolinha_2):
    bolinha_mais_pesada = bolinha_1
elif (peso_bolinha_2 > peso_bolinha_1):
    bolinha_mais_pesada = bolinha_2
else: #(peso_bolinha_1 == peso_bolinha_2)
    bolinha_mais_pesada = bolinha_3

print(f'A bolinha {bolinha_mais_pesada} é a mais pesada.')