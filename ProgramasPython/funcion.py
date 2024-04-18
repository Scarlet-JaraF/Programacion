# def multipordos():
#     print("ingrese un numero")
#     num=int(input())
#     print(num*2)

# def resta5():
#     print("ingrese un numero")
#     num=int(input())
#     print(num-5)



# def validafolio():
#     ticket_valido=False
#     folio_valido=123
#     print("ingrese el numero de folio")
#     n_folio=int(input())

#     if n_folio==folio_valido:
#         ticket_valido=True

# def suma10():
#     print("ingresa un numero")
#     num=int(input())
#     print(num+10)

# suma10()

# def suma(num1, num2):
#     resul=num1+num2
#     return resul

# print("ingresa dos numero")

# num1=int(input())
# num2=int(input())
# print(suma(num1,num2))

def area(largo,ancho):
    resul=largo*ancho
    return resul

def perimetro(largo,ancho):
    resul=(largo+ancho)*2
    return resul

print("ingrese ancho") 
ancho=int(input())
print("ingrese largo")
largo=int(input())

print("el area del rectangulo es: ", area(largo,ancho))
print("el perimetro del rectangulo es: ", perimetro(largo,ancho))


