# edad=int(input("Ingrese su edad: "))
# articulos=int(input("indique cantidad de articulos comprados: "))

# if edad>18 and articulos>1:
#     print("True")
# else:
#     print("False")
    

# año=int(input("Escriba el año: "))

# if año%4 ==0 :
#     if año%100 !=0 or año% 400 ==0:
#         print("Bisiesto")
# else:
#     print("No bisiesto") 

l="scarletjara"
lb=input("Ingrese letra que desea contar: ")
c=0
for letra in l:
    if letra==lb:
      c=c+1

print("el nombre contiene ", c, lb)
