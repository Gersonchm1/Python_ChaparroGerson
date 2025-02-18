
def conversion(f):
    b=((f*9)/5)+32
    return print(b)
def conversionc(c):
    a=((c-32)*0.555)
    return print(a)
print("Presiona 1 si quieres pasar de celsius a Fhahrenheit.")
print("Presiona 2 si quieres pasar de Fhahrenheit a Celsius.")
opcion=(input(""))


if opcion=="1":

    f=int(input("Escribe los grados Celsius para convertirlos a Fahrenheit: "))

    conversion(f)
elif opcion=="2":
    a=int(input("Escribe los grados Fahrenheit para convertirlos a Celsius: "))
    
    conversionc(a)
else:
    print("Pienselo bien amigo.")










