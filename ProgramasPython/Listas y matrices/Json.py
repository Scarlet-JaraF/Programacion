#import json

# # Datos JSON
# datos = {
#     "nombre": "Esteban",
#     "edad": 25,
#     "comuna": "Santiago",
#     "estudios": ["colegio Arturo Prat", "liceo el bosque",
#                  "Duoc UC", "Diplomado Duoc UC"]
# }

# # Abre el archivo, w es permiso de escritura
# with open('archivo.json', 'w') as archivo:
#     json.dump(datos, archivo)



# import json

# # Abrir archivo, r es permiso de lectura
# with open('archivo.json', 'r') as archivo:
#     datos_leidos = json.load(archivo)
# print(datos_leidos)
######################################################################
#Crear un archivo con la tabla solicitada. El archivo se crea con el nombre de la tabla
# num=int(input())
# nombre='tabla-'+ str(num)+ 'txt'
# with open(nombre, 'w') as archivo:
#     for i in range(1,11):
#         archivo.write(str(num)+ "x"+ str(i)+ "=" + str(num*i)+'\n')



num1=int(input())
num2=int(input())
nombre='sumade_'+ str(num1) + '_y_'+str(num2)+ '.txt'
with open(nombre, 'w') as archivo:
    archivo.write(str(num1)+ "+"+ str(num2)+ "=" + str(num1+num2)+'\n')
