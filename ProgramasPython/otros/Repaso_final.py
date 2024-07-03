# edad=int(input("Ingrese su edad: "))

# if edad>=10 and edad<18:
#     print("El valor de su ticket es $1000")
# elif edad>=18 and edad<65:
#     print("El valor de su ticket es $2000")
# elif edad>=65:
#     print("El valor de su ticket es $1500")
# else:
#     print("Su ticket es gratis :)")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# print("Este programa definira cual numero es mayor...")
# num1=int(input("Ingrese el primer numero:___"))
# num2=int(input("Ingrese el segundo numero:___"))
# num3=int(input("Ingrese el Tercer numero:___"))

# if num1>num2 and num1>num3:
#     print("El numero mayor es el ", num1)
# elif num2>num3:
#     print("Em numero mayor es el ", num2)
# else:
#     print("El numero mayor es el ", num3)
    
# +++++++++++++++++++++++++++++++++++++++++++++++++
# print("Ingrese un numero para la tabla de multiplicar")
# mul=int(input())

# print("La tabla del ", mul, "es:")
# for i in range (1,11):
#     print(mul," x ", i, " = ", mul*i)
#++++++++++++++++++++++++++++++++++++++++++++++++++
nombre=input("Ingrese el nombre del cliente:___")
total=0

while True:
    print("Seleccione una opcion del menu:")
    print("opcion 1.- Para elegir un plato del menu. ")
    print("opcion 2.- Para obtener el total de su boleta.")
    print("opcion 3.- Para salir ")
    op=int(input())
    
    match op:
        case 1:
           while True:
            print("Elija una opcion:")
            print("1. Arroz a la francesa $4.500")
            print("2. Arroz marinero $5.200")
            print("3. Sopa marinera $9.700")
            print("4. Para volver al menu principal")
            op2=int(input())
            match op2:
                case 1:
                 print("Agregado Arroz a la francesa.") 
                 total=total+4500
                
                case 2:
                  print("Agregado Arroz marinero.") 
                  total=total+5200  
                    
                case 3:
                  print("Agregado Sopa marinera.") 
                  total=total+9700 
                case 4:
                    break
                case _:
                    print("opcion no valida")    
        case 2:
            print("Señor@", nombre, "el total de su boleta es", total)
            print("Gracias por venir...")
            break
            
        case 3:
            print("Gracias por venir...")
            break
        
        case _:
            print("Opcion no valida")
                            
        