import csv
from datetime import datetime
#ahora=datetime.now()
fecha=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
registro=[]
print("Ingrese una opcion")
print("""
      1- Encender auto
      2- Estacionar auto
      4- Activar alarma
      4- Nivel de combustible bajo
      5- Nivel de aceite bajo  """)

while True:
    opc=int(input("___"))
    match opc: 
        case 1:
            registro.append(f"{fecha} Encendiendo auto...")
            registro.append(f"{fecha} Auto encendido")
            print(registro)

        case 2:
            registro.append(f"{fecha} Estacionando")
            print("Auto estacionado correctamente")

        case 3:
            print("Alarma activada")

        case 4:
            break

# def agrega_evento(evento):
#     fecha=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
#     fecha_evento= f"{fecha} - {evento}"
#     registro.append(f"{fecha} Auto encendido")
#     return(f"{evento}-{fecha}")
    

with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
    
        # Escribir una fila en el archivo CSV
        escritor_csv.writerow([registro])
        


