
def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mul(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div
        
        

operador = input("Digite um operador matematico: ")
a = int(input("Digite um valor: "))
b = int(input("Digite um valor: "))
operacao = calculadora(operador)(a, b)
print(operacao)


