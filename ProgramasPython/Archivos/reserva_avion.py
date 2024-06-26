#crear una reserva de avion
#6 asientos y 16 filas
#se debe reservar con el nombre, rut
#ademas hay 3 claes dentro edl avion: economica, turista, ejecutivo
import csv
asientos=[[[],[],[],[],[],[]],#1
          [[],[],[],[],[],[]],#2
          [[],[],[],[],[],[]],#3
          [[],[],[],[],[],[]],#4
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          [[],[],[],[],[],[]],
          ]


while True:    

    print("Bienvenido a Latam")
    print("""
 // ¿Qué desea hacer? //
1. Reservar un asiento.
2. Imprimir comprobante de reserva.
3. Verificar disponibilidad de asientos.
4. Imprimir planilla de reservas         
5. Anular reserva        
6. Salir.
    """)
    op = int(input("Seleccione una opción: "))    
    match op:
        case 1:
                asiento=int(input("Ingrese numero de asiento de 1 a 6:  ->"))
                while asiento<1 or asiento>6:
                        print("opcion invalida")
                        print("Ingrese numero de asiento de 1 a 6:  ->")
                        asiento=int(input())
                
                fila=int(input("Ingrese numero de fila de 1 a 16:  ->"))
                while fila<1 or fila>16:
                        print("opcion invalida")
                        print("Ingrese numero de fila de 1 a 16:  ->")
                        fila=int(input())
                
                if asientos[fila-1][asiento-1]:
                                print("Asiento no disponible")
                else:
                                print("Asiento disponible")
                                nombre=input("Ingrese su nombre:  ->")    
                                rut=input("Ingrese su rut:  -")
                                asientos[fila-1][asiento-1]={f"Nombre": nombre, "Rut": rut}
                                if fila-1<6:
                                 clase="Ejecutivo" 
                                elif fila>=6:
                                    clase="Turista"    
                                else:
                                    clase="Economica"

        case 2:
                print (f"Estimado pasajero, los datos de su reserva son los siguientes:")
                with open(f'reserva{fila},{asiento}.txt', 'w') as file:
                    file.write(f"Estimado pasajero, los datos de su reserva son los siguientes:\n")
                    file.write(f"Nombre: {nombre}\n")
                    file.write(f"Rut: {rut}\n")
                    file.write(f"Asiento: {asiento}\n")
                    file.write(f"fila: {fila}\n")
                    file.write(f"Clase: {clase}\n")
                    file.write(f"---.Gracias por su compra.---\n")                  

        case 3:
                        
                for e in asientos:
                    print(e)

        case 4:
            with open('archivo_reservas.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(asientos)
                              
        case 5:
                asiento=int(input("Ingrese numero de asiento de 1 a 6:  ->"))
                while asiento<1 or asiento>6:
                        print("opcion invalida")
                        print("Ingrese numero de asiento de 1 a 6:  ->")
                        asiento=int(input())
                
                fila=int(input("Ingrese numero de fila de 1 a 16:  ->"))
                while fila<1 or fila>16:
                        print("opcion invalida")
                        print("Ingrese numero de fila de 1 a 16:  ->")
                        fila=int(input())
                asientos[fila-1][asientos-1]={}
                


#f=open   
#with open('archivo_reservas.csv', 'w', newline='') as archivo_csv:
    #escritor_csv = csv.writer(asientos)

