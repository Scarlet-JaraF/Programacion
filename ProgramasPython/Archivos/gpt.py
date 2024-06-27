import time
from datetime import datetime

# Variables globales
pisos = 5
espacios_por_piso = 30
matriz_estacionamiento = [[None for _ in range(espacios_por_piso)] for _ in range(pisos)]

def encontrar_espacio_vacio():
    for piso in range(pisos):
        for espacio in range(espacios_por_piso):
            if matriz_estacionamiento[piso][espacio] is None:
                return piso, espacio
    return None, None

def registrar_llegada(patente):
    piso, espacio = encontrar_espacio_vacio()
    if piso is not None:
        matriz_estacionamiento[piso][espacio] = {
            'patente': patente,
            'hora_llegada': datetime.now()
        }
        print(f"Auto con patente {patente} estacionado en piso {piso + 1}, espacio {espacio + 1}.")
        return piso, espacio
    else:
        print("El estacionamiento está lleno.")
        return None, None

def registrar_salida(patente):
    for piso in range(pisos):
        for espacio in range(espacios_por_piso):
            info = matriz_estacionamiento[piso][espacio]
            if info and info['patente'] == patente:
                hora_llegada = info['hora_llegada']
                hora_salida = datetime.now()
                duracion = (hora_salida - hora_llegada).total_seconds() / 60
                costo = duracion * 15
                matriz_estacionamiento[piso][espacio] = None
                generar_boleta(patente, hora_llegada, hora_salida, costo)
                print(f"Auto con patente {patente} ha salido del estacionamiento.")
                return duracion, costo
    print("Auto no encontrado en el estacionamiento.")
    return None, None

def generar_boleta(patente, hora_llegada, hora_salida, costo):
    nombre_archivo = f"boleta_{patente}_{int(time.time())}.txt"
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"Patente: {patente}\n")
        archivo.write(f"Hora de Llegada: {hora_llegada.strftime('%Y-%m-%d %H:%M:%S')}\n")
        archivo.write(f"Hora de Salida: {hora_salida.strftime('%Y-%m-%d %H:%M:%S')}\n")
        archivo.write(f"Duración Total: {round((hora_salida - hora_llegada).total_seconds() / 60, 2)} minutos\n")
        archivo.write(f"Costo Total: {round(costo, 2)} pesos\n")
    print(f"Boleta generada: {nombre_archivo}")

# Ejemplo de uso
patente_llegada = input("Ingrese la patente del auto que llega: ")
registrar_llegada(patente_llegada)

# Simular una espera de algunos minutos (usar time.sleep para simular en pruebas reales)
time.sleep(3)  # Espera de 3 segundos como ejemplo

# Registrar salida y generar boleta
patente_salida = input("Ingrese la patente del auto que sale: ")
registrar_salida(patente_salida)