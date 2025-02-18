cantidaddeterminos = int(input ("Ingrese el numero hasta donde quiere que llegue la secuencia"))
if cantidaddeterminos <= 0:
    print(0)
sumatoria = 0
for i in range(1,cantidaddeterminos+1):
    if i% 2 == 0:
        sumatoria -= 1/i
    else:
        sumatoria += 1/i
print("la sumatoria dio:", sumatoria)     
## realizado :Gerson Steven Chapartro       
