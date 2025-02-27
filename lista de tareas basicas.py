# tareas.py
tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' añadida.")

def mostrar_tareas():
    if tareas:
        print("Tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas.")

while True:
    accion = input("¿Qué quieres hacer? (agregar/mostrar/salir): ")
    if accion == "agregar":
        tarea = input("Ingresa la tarea: ")
        agregar_tarea(tarea)
    elif accion == "mostrar":
        mostrar_tareas()
    elif accion == "salir":
        break