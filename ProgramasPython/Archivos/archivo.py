# while True:
#     nombre=(input("Ingrese nombre que contenga entre 5 y 20 caracteres: "))
#     l=0
#     for i in nombre:
#         l=l+1

#     if l >=5 and l <=20:
#         print("El nombre contiene " ,l, " caracteres, cumple con el rango requerido")
#         break
#     else:
#         print("El nombre contiene ",l,"caracteres, no cumple con el rango requerido")
        
        
nom=(input("Ingrese una palabra: "))
l=0
v=["a","e","i","o","u"]
for i in nom.lower():
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        l=l+1
print("Esta palabra contiene", l ," vocales.")