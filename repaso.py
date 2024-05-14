# def suma(a,b):
#  sumar = a + b
#  print(f"La suma de los argumentos es: {sumar}")
# num1 = int(input("Ingrese primer número: "))
# num2 = int(input("Ingrese segundo número: "))
# suma(num1,num2)

# x=int(input())

# resul=(x^2+(3*x)+1)/4

# print(" El resultado es:  \n", resul, " exactamente \n fin del ejercicio")

# print(type(10.09))
# print("-"*50)

# edad =15
# tiene_licencia = True
# if edad >= 18 or tiene_licencia:
#     print("Puede conducir")
# else:
#     print("No puede conducir")
    
# edad = 65

# if edad < 18:
#     print("Eres menor de edad.")
# elif 18 <= edad <= 40:
#     print("Eres adulto joven.")
# elif 41 <= edad < 65:
#     print("Eres adulto.")
# else:
#     print("Eres un adulto mayor.")


# edad = int(input ("Ingrese su edad __"))
# if edad > 0 and edad < 18:
#     print (f"Edad: {edad} ,tiene descuento de un 50% ")
# elif edad >= 18 and edad < 30:
#     print (f"Edad: {edad} ,tiene descuento de un 20%")

# elif edad >= 60:
#     print (f"Edad: {edad} ,tiene descuento de un 90%")
# else:
#     print (f"Edad: {edad} ,no aplica descuento")

user = input("ingrese su user")
pwd = int(input("Ingrese su pass"))
if user == "skrlt" and pwd == 1234 or user=="perro" and pwd ==4321:
    valorDev = int(input("Bienvenido, Ingrese el valor a devolver: "))
    if valorDev > 100000:
        print("Se dará la máxima urgencia a su devolución de dinero")
    else:
        print("El caso ha quedado registrado, le informaremos lo antes posible")
else:
    print ("Error en usuario o contraseña")