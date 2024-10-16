# Agenda de contactos: se puede crear, editar, eliminar, buscar y ver todos los contactos.

def menu_agenda():
    print("¡Hola! Bienvenido a tu agenda de contactos.")
    print("\nSelecciona una opción: ")
    print("1 - Agregar contacto.")
    print("2 - Editar contacto.")
    print("3 - Ver contactos.")
    print("4 - Eliminar contacto.")
    print("5 - Buscar contacto.")
    print("6 - Salir.")

def crear_contacto(agenda, ident):

    # A mejorar los valores ingresados para que corresponda con cada atributo, que no se repita el telefono.

    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Telefono: ")
    email = input("Email: ")
    contacto = {'Id': ident,'Nombre': nombre, 'Telefono': telefono, 'Email': email}
    agenda.append(contacto)
    ident += 1
    print(f"Se creo exitosamente el contacto {contacto}.")
    return ident

def editar_contacto(agenda):
    # A mejorar buscador ya que puede haber varios nombres o telefonos iguales.

    contacto_editar = input("Ingrese el Nombre, Telefono o Id. del contacto a editar.")

    for contacto in agenda:
        if (str(contacto['Nombre']) == contacto_editar or
            str(contacto['Telefono']) == contacto_editar or
             str(contacto['Id']) == contacto_editar):
            
            print(f"Contacto encontrado: {contacto}")

            print("¿Que deseas editar?")
            print("1 - Nombre.")
            print("2 - Telefono.")
            print("3 - Emai.")

            seleccion = input("Seleccione una opcion: ")

            if seleccion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                contacto['Nombre'] = nuevo_nombre
                print(f"Nombre actualizado a {nuevo_nombre}")

            elif seleccion == "2":
                nuevo_telefono = input("Ingrese el nuevo telefono: ")
                contacto['Telefono'] = nuevo_telefono
                print(f"Teléfono actualizado a {nuevo_telefono}")

            elif seleccion == "3":
                nuevo_email = input("Ingrese el nuevo email: ")
                contacto['Email'] = nuevo_email
                print(f"Email actualizado a {nuevo_email}")

            else:
                print("Opcion no valida.")

            print(f"Contacto actualizado: {contacto}")
            
            return


def ver_contactos(agenda):
    if agenda:
        print("\n Tus contactos agendados: ")

        for contacto in agenda:
            print(f"Id: {contacto['Id']}")
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Teléfono: {contacto['Telefono']}")
            print(f"Email: {contacto['Email']}")
            print("-" * 20)

def eliminar_contacto(agenda):
    # Se puede agregar un warning antes de eliminar, tener cuidado de atributos repetidos.

    contacto = input("Ingresa el nombre, telefono o Id. del contacto que quieres eliminar: ")
    for c in agenda:

        if (str(c['Id']) == contacto or 
            str(c['Nombre']) == contacto or 
            str(c['Telefono']) == contacto):

            agenda.remove(c)
            print(f"El contacto {c['Nombre']} se a eliminado correctamente.")
            return
        
    print(f"No se encontro el contacto {contacto}.")


def buscar_contacto(agenda):
    # A mejorar buscador ya que puede haber varios nombres o telefonos iguales.

    contacto_buscar = input("Ingresa el nombre, telefono o Id. del contacto que quieres buscar: ")

    for contacto in agenda:
        if (str(contacto['Nombre']) == contacto_buscar or
            str(contacto['Telefono']) == contacto_buscar or
             str(contacto['Id']) == contacto_buscar):
            
            print(f"Contacto encontrado: {contacto}")

        else:
            print(f"No se encontro el contacto mediante {contacto_buscar}")

def agenda_contactos():
    identificador = 1
    agenda = []

    while True:
        menu_agenda()
        opcion = input("Elige una de las opciones: ")

        if opcion == "1":
            identificador = crear_contacto(agenda, identificador)

        elif opcion == "2":
            editar_contacto(agenda)

        elif opcion == "3":
            ver_contactos(agenda)

        elif opcion == "4":
            eliminar_contacto(agenda)

        elif opcion == "5":
            buscar_contacto(agenda)
        
        elif opcion == "6":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break

        else:
            print("Por favor ingrese una de las opciones que figura en pantalla.")

agenda_contactos()