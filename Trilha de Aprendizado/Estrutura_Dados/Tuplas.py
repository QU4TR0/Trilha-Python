frutas = ("laranja", "pera", "uva",)

numeros = tuple(range(10))

nomes = (
    ("Guilherme", 21, "São Paulo"),
    ("João", 25, "São Paulo"),
    ("Mariana", 12, "Brasilia"),
    ("Gabriela", 34, "Rio de Janeiro"),
)

print(numeros)
print(frutas)

for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome[0]}")