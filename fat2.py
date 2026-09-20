n=0
fat=1
while n>=0:
   n=eval(input('Por favor,digite um número inteiro positivo, '))
   if n>=0:
      
      for i in range(1,n+1):
         
         fat=fat*i
         fat==fat
      print(f'Fatorial de {n} é igual a {fat}')
      
      fat=1
   else:
      print(f'O NÚMERO DIGITADO NÃO ATENDE À ESPECIFICAÇÃO')
