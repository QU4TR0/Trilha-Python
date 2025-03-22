# print(set([1, 2, 3, 1, 3, 4]))

# num = {1, 2, 3, 1, 3, 4}

# numeros = list(num)

# print(numeros)

# conjunto_a = {1, 2}
# conjunto_b = {3, 4}

# conjuntos = conjunto_a.union(conjunto_b)

# conjunto_a = {1, 2, 3}
# conjunto_b = {2, 3, 4}

# conjuntos = conjunto_a.intersection(conjunto_b)

# conjuntos = conjunto_a.difference(conjunto_b)
# conjunto = conjunto_b.difference(conjunto_a)

# conjuntos = conjunto_a.symmetric_difference(conjunto_b)

# conjunto_a = {1, 2, 3}
# conjunto_b = {4, 1, 2, 5, 6, 3}

# conjuntos = conjunto_a.issubset(conjunto_b)
# conjunto = conjunto_b.issubset(conjunto_a)

# conjuntos = conjunto_a.issuperset(conjunto_b)
# conjunto = conjunto_b.issuperset(conjunto_a)

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# conjuntos = conjunto_a.isdisjoint(conjunto_b)
# conjunto = conjunto_a.isdisjoint(conjunto_c)

conjunto_c.add(2)
conjunto_c.discard(0)

print(1 in conjunto_c)