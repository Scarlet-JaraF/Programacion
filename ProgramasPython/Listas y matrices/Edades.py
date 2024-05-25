import random
nombres=["Bastian", "Tomás", "Amanda"]
# edad1=random.randint(1,20)
# edad2=random.randint(1,20)
# edad3=random.randint(1,20)
# e=0
# for i in nombres:
    
    # print(f"Su numbre es {i} y su edad es {edades[e]}")
    # e=e+1
# edades=[]
# for j in range(3):
#     num=random.randint(1,20)
#     edades.append(num)

# for i in range(len(nombres)):
#     print(f"Su numbre es {nombres[i]} y su edad es {edades[i]}")

 ###################################################################################################

ingresa="Si" 
nombres=[]
while ingresa!="NO":
    nnom=input("Ingrese un nombre nuevo:   ") 
    nombres.append(nnom) 
    print("Desea a agregar otro nombre?")
    ingresa=input().upper()
# print("Los nombres ingresados son:")
# print(nombres)    
print("El nombre mas corto es ", min(nombres, key=len))
nombres.remove(min(nombres, key=len))
print(nombres)





