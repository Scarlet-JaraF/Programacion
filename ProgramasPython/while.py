# # text=""

# # while text !="hi":
# #     print("Ingrese el saludo correcto")
# #     text=input()
# # print("Ese es el saludo correcto")
 
# def ingresarpassword():

#     cont=1
    
#     print("Ingrese contraseña") 
#     password=input()
#     while password !="1234" and cont<3:
#         print("Contraseña incorrecta")
#         cont=cont+1
#         password=input()
#         if cont==3:
#             print("Cuenta bloqueada")
#         else:    
#             print("Ingresando")
# ingresarpassword()

# def comeCena():
#     cantcomida=100
     
#     while cantcomida !=0:
#         print("Desea comer?")
#         cucharada=input()
#         if cucharada=="si":
#             cantcomida=cantcomida-25
#             print("la cantidad de comida es ",cantcomida)
#         else:
#             print("Usted ya dejo de comer")
#             cantcomida=0

# comeCena()
    
# def cantidadmicros():
#     cantmicros=int(0)
#     hora=int(8)
#     #las micros pasan solo hasta las 12
#     #el usuario comienza a esperar a las 8
#     #cada vez que dice que no, pasa una hora
#     while cantmicros !=3 and hora<12:
#         print("ha pasado una micro?")
#         resp=input()
    
#         if resp=="si":
#             cantmicros=cantmicros+1
#         else:
#             hora=hora+1
#     if cantmicros==3:
#         print("Ya no hay mas micros")         
#     else:
               
        
# cantidadmicros()
           
        
    