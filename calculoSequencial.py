cont = 0
soma = 0
numero = int(input("Entre com o numero para ser calculado: "))
while cont != numero:
    cont = cont + 1
    soma = soma + cont
print(f'A soma dos numeros de {numero} até 1 é: {soma}')
