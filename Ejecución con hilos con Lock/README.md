# Ejercicio 3: Ejecución con Hilos con Lock (Condiciones de Carrera)

## Descripción del Ejemplo (Vida Diaria)
Este script de Python simula la **compra en línea del último asiento disponible para un partido de fútbol**, donde **Yo y 10 personas más (11 usuarios en total)** hacen clic en el botón **"Comprar"** exactamente en el mismo milisegundo:

1. **Escenario SIN Lock (Condición de Carrera):**  
   Al hacer clic al mismo milisegundo (sincronizados mediante `threading.Barrier`), los 11 hilos leen `asientos_disponibles > 0` antes de que el servidor termine de procesar el primer pago y descuente el boleto. Como resultado, el mismo asiento se vende 11 veces (sobreventa con saldo negativo `-10`).

2. **Escenario CON Lock (`threading.Lock`):**  
   Al proteger la sección crítica con `with lock:`, aunque los 11 usuarios hagan clic en el mismo milisegundo, el candado (`Lock`) garantiza la **exclusión mutua**: solo el primer hilo que adquiere el `Lock` compra el último boleto (`Restantes: 0`), y las otras 10 personas reciben inmediatamente el mensaje de que el asiento ya fue vendido.

## Estructura del Proyecto
- `03_hilos_lock.py`: Script de Python con `threading.Thread`, `threading.Barrier` y `threading.Lock`.
- `docker-compose.yml`: Configuración del contenedor de Docker.
- `README.md`: Instrucciones de ejecución.

## Cómo ejecutar el script con Docker

### Opción 1: Usando Docker Compose (Recomendado)
1. Abre una terminal y entra en la carpeta del ejercicio:
   ```bash
   cd "Ejecución con hilos con Lock"
   ```
2. Ejecuta el contenedor con Docker Compose:
   ```bash
   docker compose up
   ```
3. Para limpiar el contenedor al finalizar:
   ```bash
   docker compose down
   ```

