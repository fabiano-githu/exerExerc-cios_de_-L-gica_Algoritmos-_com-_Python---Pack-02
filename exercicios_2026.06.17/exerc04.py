'''
4. Verificador de Número

 - Peça um número ao usuário.
 - Informe se ele é:
    - Positivo
    - Negativo
    - Zero

Dica

 - Use: `if...elif...else`

Desafio extra

 - Informe também se o número é par ou ímpar.
'''

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("É Zero!...")

# Desafio extra
if numero != 0:
    if numero % 2 == 0:
        print("...e é Par")
    else:
        print("...e éÍmpar")