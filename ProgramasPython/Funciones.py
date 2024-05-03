def areacirculo(num):
    area=(num*num)*3.14
    return area

def areacuadrado(lado):
    area=num**2
    return area

def arearectangulo(lado1,lado2):
    area=num1*num2
    return area

def areatriangulo(base,altura):
    area=(num1*num2)/2
    return area

def perimetrocuadrado(lado):
    perimetro=lado*4
    return perimetro

print("---Bienvenido usuario admin")
print("Seleccione una opcion")
print("1.    Calcular area de un circulo")
print("2.    Calcular area de un cuadrado")
print("3.    Calcular area de un rectangulo")
print("4.    Calcular area de un triangulo")
op=int(input("Seleccione una opcion: "))


match op:
    case 1:
       print("Ingrese radio: ")
       num=int(input())
       print("El area del circulo es: "+ str(areacirculo(num)))

    case 2:
        print("Ingrese lado:")
        num=int(input())
        print("El area del cuadrado es: "+ str(areacuadrado(num)))

    case 3:
        print("Ingrese base")
        num1=int(input())
        print("Ingrese altura:")
        num2=int(input())
        print("El area del rectangulo es: "+ str(arearectangulo(num1,num2)))

    case 4:
        print("Ingrese base:")
        num1=int(input())
        print("Ingrese altura:")
        num2=int(input())
        print("El area del triangulo es: "+ str(areatriangulo(num1,num2)))

   
