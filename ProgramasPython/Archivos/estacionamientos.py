#crear edificio de estacionamientos de 5 pisos y 30 espacios por piso
#se debe registrar la petente y la hora de llegada, ademas, al salir, debe 
#calcular cuntos minutos estuvo en el estacionamiento y cobrar
#cada minuto vale 15 pesos
#debe guardar una boleta en .txt que diga los datos , hora llegada, hora salida y 
#patente y el total a cobrar
from datetime import datetime
piso=0
est=0
parking=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         ]
entrada= datetime.now()
#parking[0][0]={"patente":"ASDF11", "fecha": entrada}
#diferencia=datetime.now() - parking[0][0]["fecha"]
#print(diferencia)

def ingresar():
    print("Bienvenido")
    patente=input("Ingrese patente con el formato AABB99 0 AA8899: ").upper()
    while len(patente) !=6:
        print("Formato incorrecto, Ingrese nuevamente.")
        patente=input().upper()
        
    parking[piso][est]={"patente": patente, "entrada":entrada}
    est=est+1
    #if piso==:
    if est ==29:
        est=0
        piso=piso+1
while True:
    print("""Ingrese una opcion:
      1.- Marcar entrada
      2.- Marcar salida.""")
    op=int(input(":"))
    
            
    match op:
        case 1:
            print("Bienvenido")
            patente=input("Ingrese patente con el formato AABB99 0 AA8899: ").upper()
            while len(patente) !=6:
                print("Formato incorrecto, Ingrese nuevamente.")
                patente=input().upper()
                
            parking[piso][est]={"patente": patente, "entrada":entrada}
            est=est+1
            #if piso==:
            if est ==29:
                est=0
                piso=piso+1
            
            print (len(parking))
            
            print(parking)
            print (f"cupos {len(parking)}")
            print(est)
            print(piso)
            
            
        case 2:
            patente = (input("Ingrese el vehículo a borrar: "))
            # for n in range(0,4):
            #     for m in range(0,29):
            #         if borrar in parking[n][m]:
            #             parking[n][m].remove(borrar)
            #             print(parking)                        
            #             print(parking[n][m]["entrada"])
            #             #diferencia = datetime.now() - parking[n][m][1]
            #             #print(diferencia)
            #             registrar_salida(patente):
            for piso in range(0,4):
                for espacio in range(0,29):
                    info = parking[piso][est]
                    if info and info['patente'] == patente:
                        hora_llegada = info['entrada']
                        hora_salida = datetime.now()
                        duracion = (hora_salida - hora_llegada).total_seconds() / 60
                        costo = duracion * 15
                        parking[piso][espacio] = None
                        #generar_boleta(patente, hora_llegada, hora_salida, costo)
                        print(f"Auto con patente {patente} ha salido del estacionamiento.")
                        print (duracion, costo)
            print("Auto no encontrado en el estacionamiento.")
            #return None, None

        
        case _:        
            print("caso 3")