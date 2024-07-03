from datetime import datetime


lista=[
       [[],[],[],[],[]],
       [[],[],[],[],[]],
       [[],[],[],[],[]]
       ]

def encontrar():
    for piso in range(3):
        for cuarto in range(5):
            if lista[piso][cuarto] == []:
                return piso, cuarto
    print("no disponible")
    return None, None





def ingreso(nombre, hora):
        
        pisoo, cuart = encontrar()
        if pisoo is not None:
            lista[pisoo][cuart]={'nombre': dato1, 'hora': dato2}
        
            print(f"el piso sera {pisoo +1}, y el lugar {cuart+1}")
            print(lista)
            return pisoo, cuart, hora, nombre
            
            
def salir(nombre):
    for n in range(3):
        for m in range(5):
            cuarto=lista[n][m]
            if cuarto['nombre'] == nombre:
                salida=datetime.now()
                entrada=lista[n][m]['hora']
                cuarto=[]
                tiempo=(salida-entrada).total_seconds()/60
            print(f'''
                  hora de entrada: {entrada.strftime('%X')}
                  hora de salida: {salida.strftime('%X')}
                  ''')
            boleta(nombre, entrada, salida, tiempo )
            return tiempo, salida, entrada, dato
        print("no encontrado") 
        return None      
        
def boleta(nombre, entrada, salida, tiempo ):
    nom_archivo=nombre
    with open(f'boleta_de_{nom_archivo}.txt', 'w') as archivo:
        archivo.write(f'entrada : {entrada.strftime('%X')}\n')
        archivo.write(f'salida : {salida.strftime('%X')}')
        archivo.write(f'tiempo transcurrido {round(tiempo,2)}')
            
            
while True:
    
    print('''
          1 ingrsar
          2 salir''')
    resp=int(input("ingrese una opcion "))
    match resp:
        case 1:
 
            dato1=input('ingrese su nombre  ')
            dato2=datetime.now()
            ingreso(dato1, dato2)
        
        case 2:
            dato= input("ingrese su nombre  ")
            salir(dato)
            
            
    
 
        
            
