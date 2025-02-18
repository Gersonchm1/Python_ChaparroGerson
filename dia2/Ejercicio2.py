def IntereSimple(a,b,e):
    g=a*(1+(b/100)*e)
    return (g)
def InteresCompuesto(c,i,t):
    f=c*(1+(i/100))**t
    return(f)
print("presiona 1 si quieres hallar el interes simple:")
print("Presiona 2 si quieres hallar el interes compuesto:")
opcion=(input(""))
if opcion=="1":

    capital=int(input("Dime el capital: "))
    Interes=int(input("Dime la tasa de interes %: "))
    Tiempo=int(input("Dime la cantidad de tiempo en años: "))
    print(IntereSimple(capital,Interes,Tiempo))
elif opcion=="2":

    capital=int(input("Dime el capital: "))
    Interes=int(input("Dime la tasa de interes anual %: "))
    Tiempo=int(input("Dime la cantidad de tiempo en  años: "))
    print(InteresCompuesto(capital,Interes,Tiempo))
