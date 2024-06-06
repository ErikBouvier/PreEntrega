# declare una variable, a la que le asigne el valor de un dict vacio, donde se almacenaran los usuarios

usuarios = {}

# def para registrar usuarios


def registro_usuario():
    usuario = input("Ingrese el nombre de usuario:  ")
    if usuario in usuarios:
        print("El nombre de usuario ya existe.")
        return
    print("Usuario ingresado correctamente. \n")
    contraseña = input("Ingrese su contraseña:  ")
    usuarios[usuario] = contraseña
    print("Contraseña ingresada correctamente. \n")

# def para borrar un usuario especifico con solicitud de contraseña


def borrar_usuario():
    if not usuarios:
        print("Aún no hay usuarios registrados.")
    usuario = input("Ingrese el nombre de usuario a borrar: \n")
    if usuario not in usuarios:
        print("El usuario no está registrado.")
        return
    contraseña = input("Ingrese la contraseña del usuario: \n")
    if usuarios[usuario] == contraseña:
        del usuarios[usuario]
        print(f"El usuario {usuario} ha sido borrado con exito.")
    else:
        print("Contraseña incorrecta. No se pudo borrar el usuario.")


# def para mostrar usuarios

def mostrar_usuario():
    if not usuarios:
        print("No hay usuarios registrados \n")
        return
    for usuario, contraseña in usuarios.items():
        print(f"Usuario: {usuario} -> Contraseña: {contraseña}")


# def para loguearse

def login():
    while True:
        usuario = input("Ingrese su nombre de usuario: \n")
        if usuario not in usuarios:
            print("El usuario no esta registrado.")
            return
        contraseña = input("Ingrese su contraseña: \n")
        if usuarios[usuario] == contraseña:
            print("Login exitoso.")
            return usuario
        else:
            print("Contraseña incorrecta. Intentelo nuevamente.")
            break


# def menu para ejecutar programa


def menu():
    while True:
        print("Menú: ")
        print("1 - Registre un usuario")
        print("2 - Borrar usuario")
        print("3 - Mostrar usuarios ")
        print("4 - Login")
        print("6 - Salir")
        opcion = input("Ingrese una opción: \n")
        if opcion == "1":
            registro_usuario()
        elif opcion == "2":
            borrar_usuario()
        elif opcion == "3":
            mostrar_usuario()
        elif opcion == "4":
            login()
        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opción no valida. Por favor ingrse una opción válida. ")


# llamada a la función menu


menu()
