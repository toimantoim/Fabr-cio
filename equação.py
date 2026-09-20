import math
a=eval(input("DIGITE O COEFICIENTE DE X AO QUADRADO DA EQUAÇÃO,  "))
if a==0:
    print("ESSA EQUAÇÃO NÃO É DO SEGUNDO GRAU")
else:
    
    b=eval(input("DIGITE O COEFICIENTE DE X DA EQUAÇÃO,  "))
    c=eval(input("DIGITE O COEFICIENTE INDEPENDENTE DA EQUAÇÃO,  "))
    delta=b**2-4*a*c
    if delta<0:
        
       print("ESSA EQUAÇÃO NÃO POSSUI RAÍZES REAIS")
    else:
        
        if delta==0:
            
            print(f'ESSA EQUAÇÃO POSSUI UMA ÚNICA RAÍZ QUE É IGUAL A {-b/2*a}')
        else:
            
            print(f'ESSA EQUAÇÃO POSSUI DUAS RAÍZES X1={(-b+math.sqrt(delta))/2*a} E X2={(-b-math.sqrt(delta))/2*a}')
   
