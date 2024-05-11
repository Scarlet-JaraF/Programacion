gasto=0  
while True:
  print("--Bienvenido al sistema Python")
  print("Seleccione una opcion")
  print("1.- Escriba su nombre")
  print("2.- Igrese su gasto")
  print("3.- Mostrar resultado")
  print("4.- ingrese su año de nacimiento")
  print("5.- Opcion salir")
  print("6.- Es mayor de edad?")
  
  op=int(input())
  
  match op:
  
      case 1: 
          nombre=input("ingrese un nombre: ")
          print("Nombre", nombre, "ingresado correctamente")
          print("*******************************************")
      case 2:
          print("ingrese su gasto")
          gasto=gasto+int(input())
      case 3:
          print("Su gasto total es: ", gasto)
          print("*******************************************")
      case 4:
        #if nombre=="" and edad=="" and gastos==0:
          print("Seleccione las opciones 1, 2, 3 y ")
          añonac=int(input("Año de nacimiento: "))
          añoact=2024
          edad=añoact-añonac
          print("Usted tiene ", edad, "años y su gasto es ", gasto)
      case 5:
          break
      case 6:
          if edad>=18:
              print("Usted es mayor de edad")
          else:
              print("Usted no es mayor de edad")    

  