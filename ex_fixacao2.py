'''
-Resolver a questão: Fazer um programa que pergunte o valor da conta a ser paga no restaurante. O programa deve apresentar como resposta o valor da conta
com o acréscimo de 10% do garçom
'''

valorin = float(input("Valor da conta: R$"))

porcentagem = valorin * 0.10

valorfin = porcentagem + valorin

print("O valor da conta com o acréscimo do garçom é: R$", valorfin)