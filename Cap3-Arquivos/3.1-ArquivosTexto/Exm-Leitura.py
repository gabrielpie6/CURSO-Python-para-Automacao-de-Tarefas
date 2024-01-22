##########################################################
# Capítulo 3 - Arquivos                                  #
# EXEMPLO: Leitura de um arquivo de texto (.txt)         #
#                                                        #
##########################################################


with open("arquivoDeTexto.txt", mode='r') as arquivoTxt:
    nome = arquivoTxt.readline()            # Realizando a leitura da primeira linha do documento
    print("Nome da empresa: " + nome)       # Escrevendo no terminal o nome que esta no documento lido
    
    for iteracao in range(0, 4):            # Laco de repeticao para ler as proximas 4 linhas do documento
        linha = arquivoTxt.readline()       # Lendo o documento e armazenando em <linha>
        print(linha)                        # Escrevendo a linha lida no terminal




##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by Gabriel Pietsiaki Izidoro      #
##########################################################