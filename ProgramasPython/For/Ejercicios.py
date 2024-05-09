#ejercicio 3
# n= int(input("Introduce un numero entero positivo: "))
# for i in range(1, n+1, 2):
#     print(i, end= ",")


# for i in range (2,15,2):
#     print("imprimo esto "+str(i)+" veces")



# inv=int(input("Ingrese la cantidad de dinero que desea invertir: "))
# interes=int(input("Ingrese el interes anual: "))
# años=int(input("Ingrese numero de años: "))

# for i in range (años):
#     capital=inv+(inv*interes/100)
#     print("Su capital en el año "+str(i+1)+" es: ",capital)

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))