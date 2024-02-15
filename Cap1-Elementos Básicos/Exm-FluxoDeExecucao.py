##########################################################
# Capitulo 1 - Fluxo de Execuçao                         #
# EXEMPLO: Utilizacao de elementos do fluxo de execucao  #
#                                                        #
##########################################################


# Inicializa uma lista <valores> com cinco inteiros: 10, 15, 20, 25 e 30.
valores = [10, 15, 20, 25, 30]

# Usa a funcao print para imprimir uma string formatada que inclui a lista <valores>. 
# A lista <valores> e convertida em uma string e inserida no lugar de {valores} na string formatada.
print(f"Valores originais: {valores}")

# Imprime uma string que indica que os proximos valores impressos estarao dentro de um certo escopo.
print("VALORES DENTRO DO ESCOPO 12 <= x < 25:")

# Inicia um loop for que itera sobre cada item na lista <valores>. 
# Em cada iteracao, o item atual e atribuido a variavel <valor>.
for valor in valores:
    # Usa um teste condicional if para verificar se o <valor> atual esta dentro do escopo 12 <= x < 25.
    if (12 <= valor < 25):
        # Se a condicao for verdadeira, imprime o <valor> atual.
        print(valor)

# Inicializa uma variavel <i> com o valor 0.
# Esta variavel sera usada como contador no proximo laco de repedicao while.
i = 0

# Inicia um loop while que continua enquanto <i> for menor que o comprimento da lista <valores>.
while (i < len(valores)):
    # Dentro do loop, o valor atual na lista <valores> (ou seja, valores[i]) e multiplicado por 10,
    # e o resultado e atribuido de volta ao valor atual.
    valores[i] = valores[i] * 10
    # O contador <i> e entao incrementado em 1 unidade.
    i = i + 1

# Por fim, imprime uma string formatada que inclui a lista <valores> apos a multiplicacao.
print(f"Valores alterados: {valores}")


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by           Gabriel Pietsiaki    #
##########################################################