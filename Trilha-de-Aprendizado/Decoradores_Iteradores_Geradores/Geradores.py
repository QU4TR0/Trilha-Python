def gerador(numeros: list[int]):
    # contador += 1
    for numero in numeros:
        yield numero *2
        
for i in gerador(numeros=[1,5,4]):
    print(i)