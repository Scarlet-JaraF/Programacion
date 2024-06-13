from actividad_funciones import FuncionDiccionario
def creaDiccionario():
    
      dic_vacio={}
      while True:
         

           key=input("Ingrese una key")
           if key =="shazam":
              print(dic_vacio)
              break
              
           else:
            value=input("Ingrese el valor de key anterior")
            dic_vacio[key]=value
            print(dic_vacio)
    
      clave=str(input("ingrese numero indice"))
      resultado= FuncionDiccionario(dic_vacio, clave)

      print(resultado)   

creaDiccionario()
