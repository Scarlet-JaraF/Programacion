matriz=[
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],],
    [[],[],[],[],[],[],[],[],[],[],]
    
    ]

def conteo(con):
    
    for f in range(10):
        for a in range(10):
            if matriz[f][a]!=[]:
                con=con+1
    return print(f"total de transacciones: {con}")
            
def suma(suma):      
    for f in range(10):
            for a in range(10):
                if matriz[f][a]!=[]:
                    venta=matriz[f][a]['valor']
                    suma=suma+venta
                     
    return print(f"total de ventas es {suma}")

def disponibilidad():
    if matriz[fila-1][asiento-1] == []:
        return fila, asiento
    else:
        print("asiento no disponible")
        return None, None
    
                     
                     

def reserva(nombre, fila, asiento):
    fila, asiento=disponibilidad()
    if fila is not None:    
        if fila>=1 and fila <=3:
            valor= 10000
        elif fila>=4 and fila<=6:
            valor= 18500
        elif fila>=7 and fila<=10:
            valor= 21500
        matriz[fila-1][asiento-1]={
            'nombre': nombre,
            'rut': rut,
            'valor': valor
        }
        print(f'Usted ha reservado el asiento {asiento}, en la fila {fila}, por un valor de {valor}')
        return valor
    return( "asiento no disponible")
    
def buscar(fila, asiento):
        if matriz[fila-1][asiento-1] != []:
            print(matriz[fila-1][asiento-1])
        else: 
            print('este asiento se encuentra vacio')

def comprobante(rut):
    for f in range(10):
          for a in range(10):
            asiento_reservado = matriz[f][a]
            if asiento_reservado and asiento_reservado['rut'] == rut:
                    nombre=matriz[f][a]['nombre']
                    pago=matriz[f][a]['valor']
                    with open(f'comprobante_codigo_{rut}.txt', 'w') as archivo:
                         archivo.write('Su reserva contiene la siguiente informacion: \n')
                         archivo.write(f'nombre: {nombre}\n')
                         archivo.write(f'asiento: {a+1}\n')
                         archivo.write(f'fila: {f+1}\n')
                         archivo.write(f'monto a pagar: ${pago}\n')
                    return print('se ha generado su comprobante de reserva')
    
    return print(f'rut {rut} no encontrado')
               
while True:
    print('''
    Bienvenido!!, que desea hacer?
          1. Reservar asiento
          2. obtener informacion de un asiento
          3. ver estado de asientos
          4. Total ventas del dia
          5. Generar comprobante de reserva
          6. Salir
    ''')

    op=int(input('ingrese una opcion:  '))

    match op:
        case 1:
            nombre=input("Escriba su nombre: ")
            rut=int(input('indique su rut sin puntos ni guion: '))
            fila=int(input("escriba numero de fila de 1 a 10: "))
            while fila <1 or fila >10:
                fila=int(input("fila no existe, escriba numero de fila de 1 a 10: "))

            asiento=int(input("escriba numero de asiento de 1 a 10: "))
            while asiento <1 or asiento >10:
                asiento=int(input("asiento no existe, escriba numero de asiento de 1 a 10: "))
            reserva(nombre, fila, asiento)

        case 2:
            print('Indique n° de fila y asiento que desea revisar:')
            
            fila=int(input("escriba numero de fila de 1 a 10: "))
            while fila <1 or fila >10:
                fila=int(input("fila no existe, escriba numero de fila de 1 a 10: "))

            asiento=int(input("escriba numero de asiento de 1 a 10: "))
            while asiento <1 or asiento >10:
                asiento=int(input("asiento no existe, escriba numero de asiento de 1 a 10: "))
            buscar(fila, asiento)

        case 3:
            print(matriz)

        case 4:
            conteo(0)
            suma(0)



        case 5:
             
            rut=int(input('indique su rut sin puntos ni guion: '))
            comprobante(rut)

        case 6:
              break

        case _:
              print('opcion no valida')
