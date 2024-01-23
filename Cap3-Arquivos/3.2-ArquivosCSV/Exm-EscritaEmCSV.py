##########################################################
# Capitulo 3 - Arquivos                                  #
# EXEMPLO: Escrita de um arquivo de tabelas (.csv)       #
#                                                        #
##########################################################


import csv

cabecalho = ["Cliente", "Total a Pagar", "Total Pago"]              # Definindo um cabecalho para a tabela

# Definindo valores de clientes para inserir na tabela
cliente1 = ["Alberto", 15,  10 ]
cliente2 = ["Bianca" , 100, 0  ]
cliente3 = ["Carlos" , 50,  50 ]

clientes = [cliente1, cliente2, cliente3]                           # Unindo todos os clientes em uma unica lista

nomeDoArquivo = "tabelaClientes.txt"                                # Definindo o nome do documento a ser exportado
with open(nomeDoArquivo, mode='w') as arquivo:
    arquivoCSV = csv.writer(arquivo)                                # Acessando o arquivo como formato CSV

    arquivoCSV.writerow(cabecalho)                                  # Escrita do cabecalho da tabela no arquivo
    arquivoCSV.writerows(clientes)                                  # Escrita dos clientes


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by Gabriel Pietsiaki Izidoro      #
##########################################################