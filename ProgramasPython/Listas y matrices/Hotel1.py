import csv
hotel = [
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
]
    
while True:    

    print("Bienvenido al hotel duocuc")
    print("""
 // ¿Qué desea hacer? //
1. Reservar una habitación.
2. Check out de habitacion.
3. Verificar disponibilidad de habitaciones.
4.          
5. Salir.
    """)
    op = int(input("Seleccione una opción: "))    
    match op:
     
        case 1:
            print("elija piso")
            piso=int(input())
            print("elija habitacion")
            habitacion=int(input())

            if hotel[piso-1][habitacion-1]:
                print("Ocupada")

            else:
                print("Libre")
                nom=(input("Ingrese nombre:   "))    
                hotel[piso-1][habitacion-1]={"nombre":nom}

        case 2:
            print("elija piso")
            piso=int(input())
            while piso<1 or piso>10:
                print("opcion invalida")
                print("elija piso")
                piso=int(input())
            print("elija habitacion")
            habitacion=int(input())
            while habitacion<1 or habitacion>10:
                print("opcion invalida")
                print("elija habitacion")
                habitacion=int(input())
            
            hotel[piso-1][habitacion-1]={}


        case 3:
            for i in hotel:

                print (i)

        case 4:
            f=open 
            with open('archivo_hotel.csv', 'w', newline='') as archivo_csv:
                 escritor_csv = csv.write([hotel])
