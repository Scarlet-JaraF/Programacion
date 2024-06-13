# def funcion_sencilla():
#     print("soy una funcion")

# #llamar la funcion
# funcion_sencilla()


# def muestraPorpantalla(palabra):
#     print(palabra)

# palabra=input("escribe algo  --")
# muestraPorpantalla(palabra)    


####################################################
#funcion con argumento

# def suma(a,b):
#     suma=a+b
#     print(f"la suma de los argumentos es {suma}")

# num1=int(input("primer numero")  ) 
# num2=int(input("segundo numero") )
# suma(num1, num2)

def suma(a,b):
    sumar=a+b
    return(sumar)

num1=int(input("primer numero")  ) 
num2=int(input("segundo numero") )


print(suma(num1,num2))
