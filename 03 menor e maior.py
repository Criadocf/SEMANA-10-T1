#Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa
#deve mostrar o maior e o menor de todos os números lidos (excluindo o zero).

flag = True

n = 1
maior = 0
menor = 9999999

while n != 0:
        n = int(input())
        if n % 10 == 0:
            if n > maior:
                maior = n
            if n % 10 == 0:
                if n < menor:
                    if n != 0:
                        menor = n
                        
print(maior)
print(menor)
        

    

    