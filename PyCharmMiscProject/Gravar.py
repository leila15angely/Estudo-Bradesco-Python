arquivo = open('arqText', 'w')

arquivo.write('curso Python \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura do arquivo texto

leitura=open('arqText', 'r')
print(leitura.read())
leitura.close()
