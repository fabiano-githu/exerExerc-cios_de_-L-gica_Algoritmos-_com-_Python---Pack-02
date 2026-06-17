'''
8. Contador de Vogais

 - Peça uma palavra ao usuário.
 - Conte quantas vogais existem nela.

Exemplo:

Digite uma palavra: computador
Quantidade de vogais: 4

Dica

 - Percorra cada letra usando um loop.
'''

palavra = input("Digite uma palavra: ")

if not palavra.isalpha():
    print("\nIsso não é uma palavra!")
else:
    contador = 0

    for letra in palavra.lower():
        if letra in "aeiou":
            contador += 1

    print(f"Quantidade de vogais: {contador}")