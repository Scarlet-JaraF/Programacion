
# def programasaludo():

#     text=""

#     while text !="hi":
#         print("Ingrese el saludo correcto")
#         text=input()
#     print("Ese es el saludo correcto")

# programasaludo()


# #********************************************************
# def ingresarpassword():
#     password=""
#     print("Ingrese contraseña") 
#     password=input()
#     while password !="1234":
#         print("Contraseña incorrecta")
#         password=input()
#         print("Ingresando")
# ingresarpassword()

# #********************************************************
# # def ingresarpassword():

# #     cont=1
    
# #     print("Ingrese contraseña") 
# #     password=input()
# #     while password !="1234" and cont<3:
# #         print("Contraseña incorrecta")
# #         cont=cont+1
# #         password=input()
# #         if cont==3:
# #             print("Cuenta bloqueada")
# #         else:    
# #             print("Ingresando")
# # ingresarpassword()
# #*********************************************************

# # def comeCena():
# #     cantcomida=100
     
# #     while cantcomida !=0:
# #         print("Desea comer?")
# #         cucharada=input()
# #         if cucharada=="si":
# #             cantcomida=cantcomida-25
# #             print("la cantidad de comida es ",cantcomida)
# #         else:
# #             print("Usted ya dejo de comer")
# #             cantcomida=0

# # comeCena()
    
# # def cantidadmicros():
# #     cantmicros=int(0)
# #     hora=int(8)
# #     #las micros pasan solo hasta las 12
# #     #el usuario comienza a esperar a las 8
# #     #cada vez que dice que no, pasa una hora
# #     while cantmicros !=3 and hora<12:
# #         print("ha pasado una micro?")
# #         resp=input()
    
# #         if resp=="si":
# #             cantmicros=cantmicros+1
# #         else:
# #             hora=hora+1
# #     if cantmicros==3:
# #         print("Ya no hay mas micros")         
# #     else:

# # cantidadmicros()
# #************************************************************

# def dormir():
#     ruido=False
#     while ruido!=True:
#         print("zzZZZzZZz")
#         print("*Susurra* Hay ruido? si/no")
#         verifica=input()
#         if verifica=="si":
#             print("Ha despertado!")
#             ruido=True
#         else:
#             print("siga durmiendo")   
# dormir()




# mantener=True
# while mantener:
#     print("---Bienvenido usuario admin")
#     print("Bienvenido al programa 1.0")
#     print("1.    Verifica PAssword")
#     print("2.    Programa Saludo")
#     print("3.    Programa dormir")
#     print("4.    Salir")
#     op=int(input("Seleccione una opcion"))


#     match op:
#         case 1: 
#             ingresarpassword()
#         case 2:
#             programasaludo()
#         case 3:
#             dormir()
#         case 4:
#             mantener=False








               
        

           
        
    