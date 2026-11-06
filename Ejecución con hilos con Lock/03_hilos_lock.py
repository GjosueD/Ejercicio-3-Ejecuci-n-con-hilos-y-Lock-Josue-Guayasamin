import threading
import time

#   Yo + 10 personas más en la web intentando comprar el último asiento (11 usuarios en total)
usuarios = ["Yo"] + [f"Persona {i}" for i in range(1, 11)]
asientos_sin_lock = 1
asientos_con_lock = 1
lock = threading.Lock()
mismo_milisegundo = threading.Barrier(len(usuarios))

def comprar_sin_lock(usuario):
    global asientos_sin_lock
    mismo_milisegundo.wait()  # Los 11 hacen clic en "Comprar" exactamente al mismo milisegundo
    if asientos_sin_lock > 0:
        time.sleep(0.05)  # Simula el procesamiento del pago en el servidor web
        asientos_sin_lock -= 1
        print(f"[SIN LOCK] ALERTA: {usuario} compro el ultimo asiento. (Asientos restantes: {asientos_sin_lock})")
    else:
        print(f"[SIN LOCK] AGOTADO - {usuario}: El asiento ya no esta disponible.")

def comprar_con_lock(usuario):
    global asientos_con_lock
    mismo_milisegundo.wait()  # Los 11 hacen clic en "Comprar" exactamente al mismo milisegundo
    with lock:  # Exclusión mutua: solo un hilo verifica y compra el asiento a la vez
        if asientos_con_lock > 0:
            print(f"[CON LOCK] Procesando pago de {usuario} por el ultimo asiento...")
            time.sleep(0.05)  # Simula el procesamiento del pago seguro
            asientos_con_lock -= 1
            print(f"[CON LOCK] EXITO: {usuario} compro el ultimo asiento del partido! (Restantes: {asientos_con_lock})")
        else:
            print(f"[CON LOCK] AGOTADO - {usuario}: Lo sentimos, el ultimo asiento ya fue vendido.")

if __name__ == "__main__":
    print(" 1. SIN LOCK (Condicion de Carrera: 11 clics en 'Comprar' al mismo milisegundo) ")
    hilos_sin_lock = [threading.Thread(target=comprar_sin_lock, args=(u,)) for u in usuarios]
    for h in hilos_sin_lock: h.start()
    for h in hilos_sin_lock: h.join()

    mismo_milisegundo.reset()
    print("\n 2. CON LOCK (Solucion a la Condicion de Carrera con threading.Lock) ")
    hilos_con_lock = [threading.Thread(target=comprar_con_lock, args=(u,)) for u in usuarios]
    for h in hilos_con_lock: h.start()
    for h in hilos_con_lock: h.join()
