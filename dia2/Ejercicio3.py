def par(p):
    result=0
    if p % 2 == 0 :
        print("es un numero par",p)
    else:
        print("es un numero impar ",p)
    
    
p=0
x=0
l=0
p=int(input("Escribe el numero"))
par(p)

for i in range(1,p+1):
    if p%i==0:
        x=x+i
    if p/i==i:
        l=1
if x!=p+1:
    print(p,"es un numero compuesto")
else :
    print(p,"es un numero primo")
if l !=1:
    print("no es cuadrado")
else:
    print("es cuadrado perfecto")




