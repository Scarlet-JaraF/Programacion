#crear edificio de estacionamientos de 5 pisos y 30 espacios por piso
#se debe registrar la petente y la hora de llegada, ademas, al salir, debe 
#calcular cuntos minutos estuvo en el estacionamiento y cobrar
#cada minuto vale 15 pesos
#debe guardar una boleta en .txt que diga los datos , hora llegada, hora salida y 
#patente y el total a cobrar
import time
from datetime import datetime
piso=0
est=0
parking=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         ]


def ingresar(patente):
    
    while len(patente) !=6:
        print("Formato incorrecto, Ingrese nuevamente.")
        patente=input().upper()
    entrada= datetime.now()
    entra=entrada.strftime("%H:%M:%S")
    parking[piso][est]={"patente": patente, "entrada":entrada}
    est=est+1
    if est ==29:
        est=0
        piso=piso+1
    return piso, est, entrada
    
  



def salir(patente):    
    for n in range(4):
        for m in range(29):
            lugar=parking[n][m]
            if lugar and lugar['patente'] == patente:
                llego=parking[n][m]["entrada"]
                print(f"Hora de llegada: {llego.strftime("%X")}")
                salida= datetime.now()
                duracion = (salida - llego ).total_seconds() / 60
                costo=duracion*15
                #print(salida.strftime("%X"))
                print(f"Hora de salida: {salida.strftime("%X")}")
                boleta(patente, llego, salida, costo)
    return duracion, costo, salida


def boleta(patente, entrada, salida, costo):
    nombre_archivo=f"boleta_vehiculo_{patente}"
    with open(archivo.txt, 'w') as archivo:
        archivo.write(f"Patente: {patente}\n")
        archivo.write(f"Hora de entrada: {entrada.strftime("%H:%M:%S")}\n")
        archivo.write(f"Hora de salida: {salida.strftime("%H:%M:%S")}\n")
        archivo.write(f"Tiempo estadía: {entrada.strftime("%H:%M:%S")}\n")
        archivo.write(f"Hora de entrada: {round(salida - entrada).total_seconds() / 60, 2})\n")
        archivo.write(f"Total a paagar: {round(costo,2)})\n")
        


while True:
    print("""Ingrese una opcion:
      1.- Marcar entrada
      2.- Marcar salida.""")
    op=int(input(":"))   
    
    match op:
        
        case 1:
            print("Bienvenido")
            patente=input("Ingrese patente con el formato AABB99 0 AA8899: ").upper()
            print(ingresar(patente))
            
        case 2:
            patente = (input("Ingrese patente de su vehiculo: ")).upper()
            salir(patente)
            
            print("su boleta esta ha sido emitida...")
            
        
                     
   