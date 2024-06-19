import csv
registro=[1, 2,3]
# Sintaxis: open('nombre_del_archivo.csv', 'modo', newline='')
# Modo común: 'w' (escritura)
with open('nuevo_archivo.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    
    # Escribir una fila en el archivo CSV
    escritor_csv.writerow([registro])
    