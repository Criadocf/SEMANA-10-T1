n = int(input())
maior = n
menor = n

while n != 0:
        n = int(input())
        if n > maior and n != 0:
          maior = n
        if n < menor and n != 0:
          if n != 0:
            menor = n

        
        
if maior != 0 and menor != 0:                   
  print(maior)
  print(menor)