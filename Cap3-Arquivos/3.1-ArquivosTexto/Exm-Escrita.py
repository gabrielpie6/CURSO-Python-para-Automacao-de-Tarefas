##########################################################
# Capitulo 3 - Arquivos                                  #
# EXEMPLO: Escrita de um arquivo de texto (.txt)         #
#                                                        #
##########################################################


cabecalho = "Notas Obtidas"                                 # Definindo um cabecalho para o documento
valores = [10, 20, 30, 40]                                  # Definindo valores para escrever

nomeDoArquivo = "resultados.txt"                            # Definindo o nome do documento a ser exportado
with open(nomeDoArquivo, mode='w') as arquivoTxt:
    arquivoTxt.write(cabecalho + "\n")                      # Escrita do cabecalho no documento

    # Conversao da lista de inteiros <valores> em uma lista de strings
    # <linhas> para que possa ser escrita utilizando writelines()
    linhas = [str(valor) + "\n" for valor in valores]       
    arquivoTxt.writelines(linhas)                           # Escrita das linhas em <linhas>


##########################################################
#    (C) Copyright CODIFICA - CNPJ 02.274.882/0001-09    #
#        Code provided by Gabriel Pietsiaki Izidoro      #
##########################################################