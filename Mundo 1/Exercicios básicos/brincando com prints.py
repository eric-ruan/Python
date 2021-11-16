print('QUal o seu nome?')
nome = input()
#print('Prazer em te conhecer {}!'.format(nome))

#podemos alinhar a direita
print('Prazer em te conhecer {:>20}!'.format(nome))

#alinhado a esquerda
print('Prazer em te conhecer {:<20}!'.format(nome))

#centralizado
print('Prazer em te conhecer {:^20}!'.format(nome))

#centralizado com detalhes
print('Prazer em te conhecer {:-^20}!'.format(nome))