biblioteca={
    "001":{"titulo":"cien años de soledad","autor":"Gabriel García Márquez","año":1967},
    "002":{"titulo":"1984","autor":"George Orwell","año":1949}
}
def agregar_libro(biblioteca):
    while True:
        id=input("Ingrese el ID del libro\n")
        if id in biblioteca:
            print("el ID ya existe, escriba uno nuevo\n")
        else:
            break
    titulo=input("Agregue el título del libro\n")
    autor=input("Agrega el nombre del autor\n")
    while True:
        try:
            año=int(input("ingrese el año de publicación\n"))
            break
        except ValueError:
            print("El año debe ser un número, intente de nuevo\n")
    biblioteca[id]={"titulo":titulo,"autor":autor,"año":año}
    print(f"el libro {titulo} agregado con éxito")
def mostrar_libro(biblioteca):
    if not biblioteca:
        print("la lista está vacía\n")
    else:
        print("listado de los libros son:\n")
        for id,valor in biblioteca.items():
            print(f"ID:{id} titulo:{valor["titulo"]}, autor:{valor["autor"]}, año:{valor["año"]}")
def buscar_libro(biblioteca):
    clave=input("ingresa el ID o el título del libro\n").strip()
    for id,valor in biblioteca.items():
        if clave==id or clave.lower()==valor["titulo"].lower():
            print(f"ID:{id}, titulo:{valor["titulo"]}, autor:{valor["autor"]}, año:{valor["año"]}")
            break       
    else:
        print("libro no encontrado")
def actualizar_libro(biblioteca):
    id=input("cuál es el ID del libro que desea modificar?").strip()
    if id in biblioteca:
        libro=biblioteca[id]
        print(f"Libro encontrado: ID:{id}, titulo:{libro["titulo"]}, autor:{libro["autor"]}, años:{libro["año"]}")
        print("qué ítem desea reemplazar?")
        print("1. Título")
        print("2. autor")
        print("3. año de publicación")
        print("4. no actualizar nada")
        opcion=input("seleccione la opcion que desea modificar\n").strip()
        if opcion=="1":
            nuevo_titulo=input("Ingrese el nuevo título").strip()
            libro["titulo"]=nuevo_titulo
            print(f"el titulo ha sido actualizado")
        elif opcion=="2":
            nuevo_autor=input("Ingrese el nuevo autor:").strip()
            libro["autor"]=nuevo_autor
            print("el autor ha sido actualizado")
        elif opcion=="3":
            while True:
                try:
                    nuevo_año=input("Agregar el nuevo año de publicación")
                    libro["año"]=nuevo_año
                    print("el año ha sido actualizado")
                    break
                except ValueError:
                    print("el año debe ser un número")
        elif opcion=="4":
            print("no se realizo ningun cambio")
        else:
            print("Opción no valida, no se realizaron cambios")
    else:
        print("no se encontró libro con ese ID")
def eliminar_libro(biblioteca):
    id=input("Cuál es el ID del libro que desea eliminar?").strip()
    if id in biblioteca:
        del biblioteca[id]
        print(f"el libro con ID:{id} ha sido eliminado")
    else:
        print(f"no hay libros guardados con ID {id}")
def menu():
    while True:
        print("Bienvenido")
        print("Qué acción desea realizar?")
        print("1. Agregar libro")
        print("2. Mostrar libro")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Borrar libro")
        print("6. Salir")
        eleccion=input("Elija una opción\n").strip()
        if eleccion=="1":
            agregar_libro(biblioteca)
        elif eleccion=="2":
            mostrar_libro(biblioteca)
        elif eleccion=="3":
            buscar_libro(biblioteca)
        elif eleccion=="4":
            actualizar_libro(biblioteca)
        elif eleccion=="5":
            eliminar_libro(biblioteca)
        elif eleccion=="6":
            print("Salida con éxito")
            break
        else:
            print("escoja una opción del 1 al 5")
menu()
