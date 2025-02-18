#mostramos cual es la secuencia
print("secuencia: 1,1,2,-1,1,-2,?")
##definimos los 2 primeros numeros de la sucesion 
a=1
b=1

print("secuencia")
print("paso 1: 1")
print("paso 2: 1")
for i in range (1,6):
    if i%2==0:
        c=a-b
        a=b
        b=c
        
    else:
        c=a+b
        a=b
        b=c
        
    print("paso ",i+2,": ",c)
##realizado por: GersonChaparro