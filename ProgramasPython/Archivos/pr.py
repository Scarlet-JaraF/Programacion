import time
from datetime import datetime

parking=[[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
         ]

def asignarlugar():
    for piso in range(4):
        for lugar in range(29):
            if parking[piso][lugar] == []:
                return piso, lugar
    return None, None


def ingresar(patente):
    piso, lugar = asignarlugar()
    if piso is not None:        
        parking[piso][lugar]={"patente": patente, "entrada":datetime.now()}

        print(f"Vehiculo patente {patente} ha ingresado al estacionamiento, dirijase a piso {piso+1}, estacionamiento {lugar+1}")
        return piso, lugar
    print("no ingresado")

def salir(patente):    
    for n in range(4):
        for m in range(29):
            lugar=parking[n][m]
            if lugar['patente'] == patente:
                llego=parking[n][m]["entrada"]
                print(f"Hora de llegada: {llego.strftime("%X")}")
                salida= datetime.now()
                duracion = (salida - llego ).total_seconds() / 60
                costo=duracion*15
                print(f"Hora de salida: {salida.strftime("%X")}")
                print(f"El vehiculo patente {patente} ha salido del estacionamiento")
                print("su boleta ha sido emitida...")
                boleta(patente, llego, salida, costo)
                return duracion, costo, salida
    print(f"Vehiculo patente {patente} no encontrado")
    return None, None


def boleta(patente, entrada, salida, costo):
    nombre_archivo=f"boleta_vehiculo_{patente}"
    with open(f'{nombre_archivo}.txt', 'w') as archivo:
        archivo.write(f"Patente: {patente}\n")
        archivo.write(f"Hora de entrada: {entrada.strftime("%H:%M:%S")}\n")
        archivo.write(f"Hora de salida: {salida.strftime("%H:%M:%S")}\n")
        archivo.write(f"Tiempo de estadia: {round((salida - entrada).total_seconds() / 60, 2)} minutos\n")
        archivo.write(f"Total a pagar: ${round(costo,2)}\n")
     

while True:
    print("""Ingrese una opcion:
      1.- Marcar entrada
      2.- Marcar salida.
      3.- Mostrar estacionamientos
      4.- Salir del menu""")
    op=int(input(":"))   
    
    match op:
        
        case 1:
            print("Bienvenido")
            patente=input("Ingrese patente con el formato AABB99 0 AA8899: ").upper()
            while len(patente) !=6:
                print("Formato incorrecto, Ingrese nuevamente.")
                patente=input().upper()
            ingresar(patente)
            
            
        case 2:
            patente = (input("Ingrese patente de su vehiculo: ")).upper()
            salir(patente)
            
            
        case 3:
            print(parking)
            
        case 4:
            break
            
        case _:
            print("Opcion no valida")
            
            
            
        
                     
   