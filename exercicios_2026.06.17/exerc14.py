'''
14. Função de Cálculo de IMC

 - Crie uma função `calculate_bmi(weight, height)`
 - Retorne `weight / (height ** 2)`
 - Exemplo:

bmi = calculate_bmi(80, 1.75)

Desafio extra

 - Classifique o resultado como:

Abaixo do peso
Peso normal
Sobrepeso
Obesidade
'''


def calculando_imc(weight, height):
    return weight / height**2

imc = calculando_imc(130, 1.75)

print(imc)

if 18.5 <= imc <= 24.9:
    print("Peso normal!")

elif 25.0 <= imc <= 29.9:
    print("Sobrepeso!")

elif 30.0 <= imc <= 34.9:
    print("Obesidade Grau 1!")

elif 35.0 <= imc <= 39.9:
    print("Obesidade Grau 2!")

else:
    print("Obesidade Grau 3!")



#----------Lógica do codigo---------

'''' Lógica de funcionamento do programa:
O programa recebe o peso e a altura de uma pessoa e calcula o IMC (Índice de Massa Corporal).
O cálculo é feito dividindo o peso pela altura ao quadrado.
Em seguida, o resultado do IMC é armazenado em uma variável.
Depois disso, o programa verifica em qual faixa o IMC se encontra:
Se estiver entre 18.5 e 24.9, a pessoa está com peso normal.
Se estiver entre 25.0 e 29.9, a pessoa está com sobrepeso.
Se estiver entre 30.0 e 34.9, é classificado como obesidade grau 1.
Se estiver entre 35.0 e 39.9, é classificado como obesidade grau 2.
Caso seja maior ou igual a 40, é classificado como obesidade grau 3.
Por fim, o programa exibe a classificação correspondente ao IMC calculado.'''