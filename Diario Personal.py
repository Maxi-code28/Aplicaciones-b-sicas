import datetime
import os

def agregar_entrada():
    entrada = input("escribe el contenido del diario: ")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diario.txt", "a") as archivo:
        archivo.write(f"[{fecha}] {entrada}\n")
    print("entrada agregada")

def leer_diario():
    try:
        with open("diario.txt", "r") as archivo:
            contenido = archivo.read()
            if contenido:
                print("Diario Personal:")
                print(contenido)
            else:
                print("vacío")
    except FileNotFoundError:
        print("no existe el diario aún")

def borrar_diario():
    if os.path.exists("diario.txt"):
        os.remove("diario.txt")
        print("El diario ha sido borrado.")
    else:
        print("El diario no existe.")

while True:
    accion = input("¿qué quieres hacer el día de hoy usuario? (agregar/leer/borrar/salir): ")
    if accion == "agregar":
        agregar_entrada()
    elif accion == "leer":
        leer_diario()
    elif accion == "borrar":
        borrar_diario()
    elif accion == "salir":
        break
    else:
        print("Acción no válida. Por favor, intenta de nuevo.")