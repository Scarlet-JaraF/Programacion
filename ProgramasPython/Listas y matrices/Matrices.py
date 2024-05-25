# matriz_sencilla=[
#                 [ [1, 2, 3, 5],  [4, 5, 6]   ],
#                 [ [7, 8, 9],     [10, 11, 12]],
#                 [ [13, 14, 15],  [16, 17, 18]]
#                 ]

# array=[1, 2]

#print(matriz_sencilla[1][1])
# for elemento in matriz_sencilla[1]:
#      print(elemento)
n1=input("Ingrese nombre 1: ")
n2=input("Ingrese nombre 2: ")
n3=input("Ingrese nombre 3: ")

lista=[n1, n2, n3]

if len(lista[0]) > len(lista[1]):
    print("mayor es ", lista[0])
elif len(lista[1]) > len(lista[2]): 
    print("mayor es ", lista[1])
elif len(lista[2]) > len(lista[0]):
    print("mayor es ", lista[2])



 