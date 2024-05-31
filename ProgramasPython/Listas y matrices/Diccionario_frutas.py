productos={"frutas": {"pera": 1500, "manzana": 1500, "uva": 1800},
         "verduras": {"zanahoria": 800, "lechuga": 1490, "apio": 1900},
         "cereales": {"avena": 2000, "chocapic": 3500, "estrellitas": 3900},
         "carnes": {"vacuno":6990, "pollo": 4900, "cerdo": 5200}
         }



print(productos)
for key in productos:
        print(key)
        for l in productos[key]:
            print(l, ":",productos[key][l])
    
# grupo=input("que busca?   ")
# prod=input("producto? ")
# print(productos[grupo][prod])
# print(productos["frutas"]["pera"])

