import datetime
from datetime import datetime
import time
hora_inicial=datetime.now()
inicial_formato=(hora_inicial).strftime("%X")
print(inicial_formato)

time.sleep(30)

hora_final=datetime.now()
final_formato=hora_final.strftime("%X")
print(final_formato)
total = round((hora_final-hora_inicial).total_seconds() /60,2)
print(total)
#print(f"{round(total,2)} minutos")
costo=total *15

with open(f"creado_a_las_.txt", 'w') as archivo:
    archivo.write(f'hora inicial {inicial_formato}\n')
    archivo.write(f'hora salida {final_formato}\n')
    archivo.write(f'tiempo transcurrido {round(total,2)} minutos\n')
    archivo.write(f'monto a pagar ${costo}\n')
                      
