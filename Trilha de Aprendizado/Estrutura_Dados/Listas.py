# numeros = list(range(11))

# print(numeros[10])


# nomes = [
#     ["Guilherme", 21, "São Paulo"],
#     ["João", 25, "São Paulo"],
#     ["Mariana", 12, "Brasilia"],
#     ["Gabriela", 34, "Rio de Janeiro"],
# ]

# for indice, nome in enumerate(nomes):
#     print(f"{indice}: {nome[0]}")

# numeros = [1, 30, 21, 2, 9, 65, 34]

# numeros.append(int(input("Digite um número: ")))

# numeros.sort()

# pares = [numero for numero in numeros if numero % 2 == 0]
# quadrado = [numero ** 2 for numero in numeros]

# print(numeros, pares, quadrado)


numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(numeros)