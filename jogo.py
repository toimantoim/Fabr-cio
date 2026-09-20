import random
números=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
a=eval(input('ESCOLHA O PRIMEIRO NÚMERO: '))
b=eval(input('ESCOLHA O SEGUNDO NÚMERO:  '))
c=eval(input('ESCOLHA O TERCEIRO NÚMERO:  '))
d=eval(input('ESCOLHA O QUARTO NÚMERO:  '))
e=eval(input('ESCOLHA O QUINTO NÚMERO:  '))
f=eval(input('ESCOLHA O SEXTO NÚMERO:  '))
palpite=[a,b,c,d,e,f]
i=0
sorteio1=random.choice(números)
sorteio2=random.choice(números)
sorteio3=random.choice(números)
sorteio4=random.choice(números)
sorteio5=random.choice(números)
sorteio6=random.choice(números)
sorteio=[sorteio1,sorteio2,sorteio3,sorteio4,sorteio5,sorteio6]
for x in palpite:
    if x in sorteio:
        i=i+1
print(f'Você teve {i} acertos e os números sorteados foram {sorteio}')        
