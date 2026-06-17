
'''1. Cadastro Simples

Crie variáveis para armazenar:

Nome
Idade
Cidade
Exiba uma frase no formato:

Meu nome é João, tenho 25 anos e moro em São Paulo.
Desafio extra
Exiba também quantos anos faltam para a pessoa completar 100 anos.'''





cad_simples = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

faltam = 100 - cad_simples["idade"]

print(f"Meu nome é {cad_simples['nome']}, tenho {cad_simples['idade']} anos e moro em {cad_simples['cidade']}.")
print(f"Faltam {faltam} anos para eu completar 100 anos.")