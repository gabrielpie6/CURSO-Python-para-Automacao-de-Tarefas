##########################################################
# Capitulo 1 - Conjunto de Dados                         #
# EXEMPLO: Utilizacao de listas para organizar           #
#          departamentos de uma empresa                  #
##########################################################


# Inicializa uma lista <departamentos> com os deparamentos de uma empresa
departamentos = ["Financeiro", "Marketing", "RH", "Juridico"]
# Usa a funcao print para imprimir uma string formatada que inclui a lista <departamentos>.
print(f"ORIGINAL: {departamentos}")

# Chama o metodo sort() na lista <departamentos> para ordenar seus elementos em ordem alfabetica.
departamentos.sort()
# Imprime a lista <departamentos> apos a ordenacao.
print(f"ORDENADO: {departamentos}")

# Usa o metodo append() para adicionar a string "Contabilidade" ao final da lista <departamentos>.
# Agora, o departamento "Contabilidade" estara incluso na lista de departamentos da empresa
departamentos.append("Contabilidade")
# Imprime a lista <departamentos> apos a insercao.
print(f"COM INSERCAO: {departamentos}")

# Usa o metodo copy() para criar uma copia da lista <departamentos> e atribui a copia a variavel <copia>.
copia = departamentos.copy()

# Usa o metodo index para encontrar o indice do elemento "Marketing" na lista <departamentos>
# e imprime o indice em qual se encontra.
print(f'INDICE: {departamentos.index("Marketing")}')

# Usa o metodo pop() para remover o elemento no indice 0 (inicio) da lista <departamentos>.
departamentos.pop(0)
# Imprime o novo indice do elemento "Marketing" na lista <departamentos> apos a remocao.
print(f'INDICE: {departamentos.index("Marketing")}')
# Imprime a lista <departamentos> apos a remocao.
print(f"COM REMOCAO: {departamentos}")


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by           Gabriel Pietsiaki    #
##########################################################