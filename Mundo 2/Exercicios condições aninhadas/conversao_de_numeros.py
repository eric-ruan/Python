'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para binário
-2 para octal
-3 para hexadecimal'''

print('Digite um número inteiro, vamos converte-lo...')
numb = int(input())
print('DIGITE...\n','-=-'*20,'\n[1] PARA BINÁRIO \n','-=-'*20,'\n[2] PARA OCTAL \n','-=-'*20, '\n[3] PARA HEXADECIMAL')
conver = int(input())

if conver == 1:
    print('O número {} convertido para BINÁRIO fica {}'.format(numb, bin(numb)[2:]))
    
elif conver == 2:
    print('O número {} convertido para OCTAL fica {}'.format(numb, oct(numb)[2:]))
    
elif conver == 3:
    print('O número {} convertido para HEXADECIMAL fica {}'.format(numb, hex(numb)[2:]))
    
else:
    print('Digite uma opção válida!')