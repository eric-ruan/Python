frase = 'Curso de Python'
print(frase[9]) #Dessa forma printa somente o caracter 9 no caso o 'P'
print('-'*10)
print(frase[7:11]) #Começa no indice 7 e printa até o caracter 6, no caso o 'e Py'
print('-'*10)
print(frase[2:11:2]) #Começa no caracter 2, printa até o 10 pulando de 2 em 2, no caso 'rod y'
print('-'*10)
print(frase[:6]) #começa no 0 e printa até o caracter 5, nesse caso 'Curso'
print('-'*10)
print(frase[9:]) #Printa do 9 até o final, 'Python'
print('-'*10)
print(frase[2::2]) #Começa no caracter 2 e vai até o final pulando de 2 em 2, 'rod yhn'
print('='*10)


print(len(frase)) #É usado na análise de Strings, conta quantos caracteres tem.
print('-'*10)
print(frase.count('a')) #vai contar quantas vezes aparece a letra 'a' dentro da frase
print('-'*10)
print(frase.count('o', 3, 15)) #começa a contagem no caracter 3 e vai até o 15, dessa forma vai contando quantas letras 'o' aparecem
print('-'*10)
print(frase.find('rso'))# te mostra onde está localizado os caracters escolhidos. OBS: quando escolhemos um valor que não tem na String, é retornado -1
print('='*10)


print('Curso' in frase)# Te retorna uma condição, 'Dentro de frase tem 'curso' '
print('='*10)


print(frase.replace('Curso','Explicação')) #substitui uma palavra por outra, de forma secundária, não diretamente na String, nesse caso a plavra 'curso' por 'explicação'
print('-'*10)
print(frase.upper())#DEIXA TUDO EM MAIUSCULO
print(frase.lower())#deixa tudo em minusculo
print(frase.capitalize())#Deixa somente a primeira letra da frase em maiusculo
print(frase.title())#Vai Deixar Cada Caracter Depois Do Espaço Em Maiusculo
print('='*10)


print(frase.strip())#'    <-Remove todos os espaços não alocados no começo e no final da frase->    '
print(frase.rstrip())#'    Remove somente os espaços não alocados da direita->     '
print(frase.lstrip())#'    <-Remove somente os espaços não alocados da direita     '
print('='*10)


print(frase.split())#Cria varias Strings, elas são criadas toda vez que aparecer um espaço entre as letras
print('-'.join(frase))#Junta a String e separa por -
