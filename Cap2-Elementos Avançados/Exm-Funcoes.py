##########################################################
# Capitulo 2 - Funcoes                                   #
# EXEMPLO: Utilizacao de funcoes para uma loja           #
#                                                        #
##########################################################


# Define uma funcao chamada <calcularImposto> que recebe dois argumentos: <valorProduto> e <taxa>.
def calcularImposto(valorProduto, taxa):
    # Calcula o imposto seguindo a regra abaixo
    imposto    = valorProduto * taxa/100.0 + 1.0/(valorProduto + 1)
    # Calcula o montante <valorTotal> adicionando o <imposto> ao <valorProduto>.
    valorTotal = valorProduto + imposto
    # Retorna o <valorTotal>.
    return valorTotal

# Define uma funcao chamada <apresentarVitrine> que recebe dois argumentos: <nomes> e <valores>.
def apresentarVitrine(nomes, valores):
    # Imprime uma string indicando o inicio da vitrine de produtos.
    print("[VITRINE DE PRODUTOS]")
    # Laco de repeticao for que itera sobre cada item na lista <nomes>. 
    # Em cada iteracao, o item atual e atribuido a variavel <i>.
    for i in range(0, len(nomes)):
        # Imprime uma string formatada que inclui o nome e o valor do produto atual.
        print(f"PRODUTO: {nomes[i]:11s} PRECO: R${valores[i]:.2f}")

# Lista de nomes dos produtos que estao no catalogo da loja
produtos     = ["Caneta", "Estojo", "Régua"]
# Lista de precos brutos dos produtos que estao no catalogo da loja
precosBrutos = [5, 30, 15]
# Lista de taxas para cada produto no catalogo da loja
taxasBase    = [20, 10, 5]

# Inicializa uma lista vazia chamada <precoFinal>.
precoFinal   = []
# Laco de repeticao for que itera sobre cada item na lista <precosBrutos>. 
# Em cada iteracao, o item atual e atribuido a variavel <i>.
for i in range(0, len(precosBrutos)):
    # Chama a funcao <calcularImposto> com o preco bruto e a taxa base do produto atual
    # e atribui o resultado a variavel <valor>.
    valor = calcularImposto(precosBrutos[i], taxasBase[i])
    # Adiciona o <valor> a lista <precoFinal>.
    precoFinal.append(valor)

# Chama a funcao <apresentarVitrine> com as listas <produtos> e <precoFinal>.
apresentarVitrine(produtos, precoFinal)


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by           Gabriel Pietsiaki    #
##########################################################