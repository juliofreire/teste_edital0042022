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
num_bolinhas = np.arange(9)

# peso das bolinhas gerado aleatoriamente
peso_padrao = np.random.rand(1)
peso_bolinha = peso_padrao * np.ones([n_bolinhas])

# adicionado peso a mais em uma das bolinhas, aleatoriamente
n_rand = np.random.randint(n_bolinhas)
peso_bolinha[n_rand] += np.random.rand(1)

# embaralhamente das bolinhas
np.random.shuffle(num_bolinhas)

# separação em 3 grupos
grupo_1 = num_bolinhas[0:3]
grupo_2 = num_bolinhas[3:6]
grupo_3 = num_bolinhas[6:9]

# pesagem de dois grupos de bolinhas
peso_g1 = np.sum(peso_bolinha[grupo_1])
peso_g2 = np.sum(peso_bolinha[grupo_2])
# peso_g3 = np.sum(peso_bolinha[grupo_3])

grupo_menor=np.array([])

# comparação dos grupos de bolinhas (papel da balança)
# seleção do grupo de bolinhas mais pesado
print("Realizando a primeira pesagem e comparação...\n")
if (peso_g1 > peso_g2):
    grupo_menor = grupo_1
    print('O Grupo 1 de bolinhas é o mais pesado, formado pelas bolinhas: ' + str(grupo_1) + '\n')
elif (peso_g2 > peso_g1):
    grupo_menor = grupo_2
    print('O Grupo 2 de bolinhas é o mais pesado, formado pelas bolinhas: ' + str(grupo_2) + '\n')
elif (peso_g1 == peso_g2):
    grupo_menor = grupo_3
    print('O Grupo 3 de bolinhas é o mais pesado, formado pelas bolinhas: ' + str(grupo_3) + '\n')

##### SEGUNDA PESAGEM

# embaralhamente do segundo grupo de bolinhas
np.random.shuffle(grupo_menor)

# divisão em 3 grupos menores

grupo_menor_1 = grupo_menor[0]
grupo_menor_2 = grupo_menor[1]
grupo_menor_3 = grupo_menor[2]

# pesagem de 2 grupos de bolinhas
peso_menor_g1 = np.sum(peso_bolinha[grupo_menor_1])
peso_menor_g2 = np.sum(peso_bolinha[grupo_menor_2])

# peso_g3 = np.sum(peso_bolinha[grupo_menor_3])

# comparação dos pesos do grupo menor
# seleção da bolinha mais pesada
print("Realizando a segunda pesagem e comparação...\n")

if (peso_menor_g1 > peso_menor_g2):
    grupo_menor = grupo_menor_1
    print('A bolinha ' + str(grupo_menor) + ' é a mais pesada.')

elif (peso_menor_g2 > peso_menor_g1):
    grupo_menor = grupo_menor_2
    print('A bolinha ' + str(grupo_menor) + ' é a mais pesada.')

elif (peso_menor_g1 == peso_menor_g2):
    grupo_menor = grupo_menor_3
    print('A bolinha ' + str(grupo_menor) + ' é a mais pesada.')