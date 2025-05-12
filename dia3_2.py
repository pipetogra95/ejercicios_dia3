agenda={}
def agregar_contacto(agenda):
        nombre=input("agrega el nombre del contacto\n").strip()
        if nombre in agenda:
            print("Ya existe un contacto con este nombre")
        else:
            telefono=input(f"agregue el telefono de {nombre}\n").strip()
            email=input(f"Ingrese el email de {nombre}\n").strip()
            agenda[nombre]={"telefono":telefono,"email":email}
            print(f"contacto {nombre} agregado éxitosamente")
def actualizar_contacto(agenda):
        nombre=input("Cuál es el nombre del contacto a actualizar\n").strip()
        if nombre in agenda:
            nuevo_telefono=input("agrega el número nuevo o enter si no desea modificar\n").strip()
            nuevo_email=input("agrega el nuevo correo o enter si no desea modificar\n").strip()
            print(f"contacto {nombre} actualizado correctamente")
            agenda[nombre]={"telefono":nuevo_telefono,"email":nuevo_email}
        else:
            print("No existe contacto con ese nombre")
def lista_contacto(agenda):
    if not agenda:
        print("No hay contactos guardados\n")
    else:
        print("lista de contactos:")
        for nombre,datos in agenda.items():
            print(f"{nombre} telefono:{datos["telefono"]}, email:{datos["email"]}")
def eliminar_contacto(agenda):
    nombre=input("cual es el nombre del contacto a eliminar?")
    if nombre in agenda:
        del agenda[nombre]
        print(f"{nombre} ha sido eliminado")
    else:
        print("no hay un contacto registrado con ese nombre")
def busqueda_contacto(agenda):
    nombre=input("nombre del contacto que desea la información")
    if nombre in agenda:
        print(f"{nombre}: telefono:{agenda[nombre]["telefono"]}, email:{agenda[nombre]["email"]}")
    else:
        print("no hay contactos con ese nombre")
def menu():
    while True:
        print("bienvenido")
        print("Qué desea hacer?")
        print("1. agregar un contacto")
        print("2. lista de contactos")
        print("3. buscar un contacto")
        print("4. actualizar un contacto")
        print("5. eliminar un contacto")
        print("6. salir")
        opcion=input("que opcion necesitas ejecutar?\n").strip()
        if opcion=="1":
            agregar_contacto(agenda)
        elif opcion=="2":
            lista_contacto(agenda)
        elif opcion=="3":
            busqueda_contacto(agenda)
        elif opcion=="4":
            actualizar_contacto(agenda)
        elif opcion=="5":
            eliminar_contacto(agenda)
        elif opcion=="6":
            print("salida con exito")
            break
        else:
            print("Debes escoger una opción entre 1 y 6")
menu()