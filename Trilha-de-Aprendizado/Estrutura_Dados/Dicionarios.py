# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# pessoa = {"nome": f"{nome}", "idade":f"{idade}"}

pessoas = {
    "Pessoa 1:": {"nome": "Guilherme", "idade":"21"},
    "Pessoa 2:": {"nome": "Pedro", "idade":"24"},
    "Pessoa 3:": {"nome": "Mariana", "idade":"22"},
}

# pessoa = dict(nome = f"{nome}", idade = f"{idade}")

# print(pessoa)

# for chave, valor in pessoas.items():
#     print(chave, valor)

# contatos = dict.fromkeys(["nome", "telefone"], "vazio")

# print(pessoas.keys())

pessoas["Pessoa 1:"].setdefault("telefone", "3333-4455")

pessoas.update({"Pessoa 1:":{"nome": "Gui Pontes"}})

print(pessoas)