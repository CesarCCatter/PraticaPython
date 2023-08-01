'''
-Resolver a questão: Fazer um programa que pergunte o valor da conta a ser paga no restaurante. O programa deve apresentar como resposta o valor da conta
com o acréscimo de 10% do garçom
'''

valorin = float(input("Valor da conta:"))

porcentagem = valorin * 0.10

valorfin = porcentagem + valorin

print("o valor da conta com o acrécimo do garçom é: ", valorfin)