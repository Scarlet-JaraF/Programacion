

gasto=0
while True:

   print("--Bienvenido al sistema Python")
   print("Seleccione una opcion")
   print("1.- Escriba su nombre")
   print("2.- Igrese su gasto")
   print("3.- Ingrese su año de nacimiento")
   print("4.- Ver resultados")
   print("5.- Opcion salir")
   opcion=int(input())
   
   match opcion:
       case 1:
           nombre=input("Escriba nombre aqui:  ")
       case 2:
           gasto=gasto+int(input("gasto aqui:  "))
       case 3:
           año=int(input("Año de nacimiento aqui: "))
           edad=2024-año
       case 4:
           print("Hola ",nombre, ", su edad es ", edad, "Usted ha gastado " , gasto)

           print("*************************************************************")
       case 5:
           print("Saliendo...")
           break

       case _:
           print("no valido")