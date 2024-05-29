lista=[[], 
       [], 
       [], 
       []]


while True:
    print(""""Ingrese una opcion:
    1.- Ingresar un vehículo
    2.- Listar vehículos
    3.- Borrar un vehículo
    4.- Conteo de vehículos
    5.- Salir
          """
          )
    op=int(input())

    match op:

        case 1: 
           while True: 
            print("Seleccione el piso ")
            piso=int(input())
            print("Ingrese patente con el formato AABB99 0 AA8899")

            pat=input().upper()
            if len(pat)!=6:
               print("Formato incorrecto")
            else:
                lista[piso-1].append(pat)
            sino=input("Desea ingresar otro vehiculo? si/no").upper()
            if sino=="NO":
                break

        
        case 2:
           while True: 
            print("""
            1.- Listar todos
            2.- Listar un piso específico
            3.- Volver""")
            opp=int(input())
            match opp:
                case 1:
                    print(lista)
                case 2:
                    print("Listar un piso específico")
                    torre=int(input())
                    print(lista[torre-1])
                case 3:
                    break
 
        case 3:
            print("Ingrese el vehículo a borrar")
            borrar=input().upper()
            lista.remove(borrar)

        case 4:
            while True:  
              print("""
                  1.- Mostar cantidad de vehículos en total
                  2.- Mostar cantidad de vehículos por piso
                  3.- Mostar cantidad de vehículos de un piso
                  4.- Volver
                  """)
              opcion=int(input())
              t=0
              match opcion:
                case 1:
                    for i in lista:
                       t=t+1
                    print(lista)   
                    print(t)
                case 2:    
                    p=int(input("Ingrese Piso"))
                    for i in lista[p-1]:
                       t=t+1
                    print(lista[p-1])   
                    print(t)

                case 3:
                    p=int(input("Ingrese Piso"))
                    for i in lista[p-1]:
                       t=t+1
                    print(lista[p-1])   
                    print(t)

                case 4:
                    break
                       
                       
               

        case 5:
            break    

        case _:

            print("Opcion no válida")    
       
       
        #    while True: 
        #     print("""
        #     1.- Listar todos
        #     2.- Listar un piso específico
        #     3.- Volver""")
        #     opp=int(input())
        #     match opp:
        #         case 1:
        #             print(lista)
        #         case 2:
        #             print("Listar un piso específico")
        #             torre=int(input())
        #             print(lista[torre-1])
        #         case 3:
        #             break