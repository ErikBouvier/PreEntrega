# declare una variable, a la que le asigne el valor de un dict vacio, donde se almacenaran los usuarios

usuarios = {}

# def para vlaidar contraseña


def validar_contraseña(usuario, contrasena):
    if usuarios[usuario] == contrasena:
        return True
    else:
        return False


# def para buscar un usuario particular


def buscar_usuario(usuario):
    if usuario.lower in usuarios:
        return True
    else:
        return False

# def para registrar usuarios


def registro_usuario(usuario):
    try:
        if len(usuario) <= 0:
            print("Por favor ingrese un dato valido: ")
            return
        if buscar_usuario(usuario):
            print("El nombre de usuario ya existe.")
            return
        print("Usuario ingresado correctamente. ")
        contraseña = input("Ingrese su contraseña: ")
        usuarios[usuario] = contraseña
        print("Contraseña ingresada correctamente.\n")
    except Exception as e:
        print(f"Error inesperado {e}")

# def para borrar un usuario especifico con solicitud de contraseña


def borrar_usuario(usuario):
    if not usuarios:
        print("Aún no hay usuarios registrados.")
    if buscar_usuario(usuario):
        print("El usuario no está registrado.")
        return
    contraseña = input("Ingrese la contraseña del usuario: ")
    if validar_contraseña(usuario, contraseña):
        del usuarios[usuario]
        print(f"El usuario {usuario} ha sido borrado con exito.\n")
    else:
        print("Contraseña incorrecta. No se pudo borrar el usuario.\n")


# def para mostrar usuarios

def mostrar_usuario(usuario):
    if usuario in usuarios:
        print(f"Usuario: {usuario} -> Contraseña: {usuarios[usuario]}")
        return



# def para loguearse

def login(usuario):
    while True:
        if buscar_usuario(usuario):
            print("El usuario no esta registrado.\n")
            return
        contraseña = input("Ingrese su contraseña: ")
        if validar_contraseña(usuario, contraseña):
            print("Login exitoso.\n")
            return usuario
        else:
            print("Contraseña incorrecta. Intentelo nuevamente.\n")
            break


# def menu para ejecutar programa


def menu():
    while True:
        print("Menú: ")
        print("1 - Registrar usuario")
        print("2 - Borrar usuario")
        print("3 - Buscar usuario")
        print("4 - Mostrar usuarios ")
        print("5 - Login")
        print("6 - Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            usuario = input("Ingrese el nombre de usuario: ")
            registro_usuario(usuario)
        elif opcion == "2":
            usuario = input("Ingrese el nombre de usuario a borrar: ")
            borrar_usuario(usuario)
        elif opcion == "3":
            usuario = input("Ingrese el nombre de usuario que desea buscar: ")
            mostrar_usuario(usuario)
        elif opcion == "4":
            for usuario in usuarios:
                mostrar_usuario(usuario)
        elif opcion == "5":
            usuario = input("Ingrese su nombre de usuario: ")
            login(usuario)
        elif opcion == "6":
            print("Saliendo del programa")
            break
        else:
            print("Opción no valida. Por favor ingrse una opción válida. ")


# llamada a la función menu


menu()

