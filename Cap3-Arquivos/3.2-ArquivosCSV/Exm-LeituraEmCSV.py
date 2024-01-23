##########################################################
# Capitulo 3 - Arquivos                                  #
# EXEMPLO: Leitura de um arquivo de tabelas (.csv)       #
#                                                        #
##########################################################


import csv

nomeDoArquivo = "tabelaClientes.txt"                        # Definindo o nome do documento a ser importado
with open(nomeDoArquivo, mode='r') as arquivo:
    arquivoCSV = csv.reader(arquivo)

    # Dois lacos de repeticao para percorrrer a tabela do arquivo CSV
    for linha in arquivoCSV:
        for celula in linha:
            print("{0:15s}".format(celula), end="")         # Escrita da celula com formato especial
        print("")


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by Gabriel Pietsiaki Izidoro      #
##########################################################