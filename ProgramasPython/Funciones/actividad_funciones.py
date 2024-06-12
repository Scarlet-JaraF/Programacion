colores=["verde", "rosado", "naranja"]


def FuncionLista():
   for i in colores:
      print(i)

#FuncionLista()      

numeros=[1,2,3,4,5,6,7,8,9]
pares=[]
impares=[]

def FuncionNumeros():
    for i in numeros:
       if i %2==0:
          pares.append(i)
       elif i %2!=0:
          impares.append(i)

    print(f"pares: {pares}")
    print(f"impares: {impares}")

#FuncionNumeros()       

# dicc={
#       "Edad": 10,
#       "Año nac": 2014
#       }
def FuncionDiccionario(dicc,key):
    if key in dicc:
       return dicc[key]
    else:
       return f"la clave '{key}' no existe"

dicc={"a": 10,"b": 2014, "c": 58}   
clave=str(input("ingrese numero indice"))

resultado= FuncionDiccionario(dicc, clave)

print(resultado)      
   

