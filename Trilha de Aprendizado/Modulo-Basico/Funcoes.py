## Args e Kwargs: *args vem como tupla e o **kwargs como um dicionário


# # def exibir_poema(data_extenso, *args, **kwargs):
# def exibir_poema(data_extenso, *lista, **dicionario):
#     texto = "\n".join(lista)
#     meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
#     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
#     print(mensagem)

# exibir_poema("Seg, 03 de Marco de 2025", "Zen of Python", "Beatiful is better than ugly.", autor="Tim Peters", ano=1999)

salario = 2000

def salario_bonus(salario, bonus):
    salario += bonus
    return salario

print(salario_bonus(salario, 500))
