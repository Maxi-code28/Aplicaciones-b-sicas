agenda = []

def agregar_contacto(nombre, numero):
    contacto = {"nombre": nombre, "numero": numero}
    agenda.append(contacto)
    print(f"Añadiste un contacto nuevo: {nombre} con el número {numero}")

def mostrar_contacto():
    if agenda:
        print("Hay contactos disponibles:")
        for i, contacto in enumerate(agenda, 1):
            print(f"{i}. Nombre: {contacto['nombre']}, Número: {contacto['numero']}")
    else:
        print("No hay contactos por mostrar")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Número: {contacto['numero']}")
            return
    print("Contacto no encontrado")

def borrar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            agenda.remove(contacto)
            print(f"El contacto {nombre} fue eliminado de la agenda")
            return
    print("Contacto no encontrado")

while True:
    accion = input("¿Qué quieres hacer el día de hoy? (agregar, mostrar, salir, buscar, borrar): ")
    if accion == "agregar":
        try:
            nombre = input("Ingresa el nombre del contacto: ")
            if nombre.isnumeric():
                raise ValueError("El nombre no puede contener números")
            numero = input("Ingresa el número del contacto: ")
            if not numero.isnumeric():
                raise ValueError("El número debe contener solo dígitos")
            agregar_contacto(nombre, numero)
        except ValueError as e:
            print(e)
    elif accion == "mostrar":
        mostrar_contacto()
    elif accion == "buscar":
        try:
            nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
            if nombre.isnumeric():
                raise ValueError("El nombre no puede contener números")
            buscar_contacto(nombre)
        except ValueError as e:
            print(e)
    elif accion == "borrar":
        try:
            nombre = input("Ingresa el nombre del contacto que deseas borrar: ")
            if nombre.isnumeric():
                raise ValueError("El nombre no puede contener números")
            borrar_contacto(nombre)
        except ValueError as e:
            print(e)
    elif accion == "salir":
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")

