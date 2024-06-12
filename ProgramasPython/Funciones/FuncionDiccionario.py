
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
    

creaDiccionario()
