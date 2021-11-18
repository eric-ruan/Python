'''Crie um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obsesidade mórbita'''

print('Digite seu peso e sua altura, vamos calcular o IMC')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)

if imc < 18.5:
    print('Você está abaixo do peso.')

elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal!')
    
elif imc >= 25 and imc <= 30:
    print('Sobrepeso.')
    
elif imc >= 30 and imc <= 40:
    print('Obsesidade.')
    
else:
    print('Obesidade mórbita.')