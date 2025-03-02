import datetime

class Nota:
    def __init__(self, texto, fecha=None):
        self.texto = texto
        self.fecha = fecha if fecha else datetime.datetime.now().strftime("%Y-%m-%d")

    def mostrar(self):
        return f"[{self.fecha}] {self.texto}"

def guardar_nota(nota, archivo="notas.csv"):
    with open(archivo, "a") as f:
        f.write(f"{nota.fecha},{nota.texto}\n")
    print("Nota guardada.")

def leer_notas(archivo="notas.csv"):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            if lineas:
                print("Notas:")
                for linea in lineas[1:]:  # Salta encabezado
                    fecha, texto = linea.strip().split(",", 1)
                    print(f"{fecha}: {texto}")
            else:
                print("No hay notas.")
    except FileNotFoundError:
        print("No hay archivo de notas aún.")

def borrar_nota(fecha, archivo="notas.csv"):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            f.write(lineas[0])  # Escribir el encabezado
            for linea in lineas[1:]:
                if not linea.startswith(fecha):
                    f.write(linea)
        print("Nota borrada.")
    except FileNotFoundError:
        print("No hay archivo de notas aún.")

# Encabezado inicial
with open("notas.csv", "w") as f:
    f.write("fecha,texto\n")

while True:
    accion = input("¿Qué hacer? (agregar/leer/borrar/salir): ")
    if accion == "agregar":
        texto = input("Texto de la nota: ")
        nota = Nota(texto)
        guardar_nota(nota)
    elif accion == "leer":
        leer_notas()
    elif accion == "borrar":
        fecha = input("Fecha de la nota a borrar (YYYY-MM-DD): ")
        borrar_nota(fecha)
    elif accion == "salir":
        break
    else:
        print("Acción no válida. Por favor, intenta de nuevo.")