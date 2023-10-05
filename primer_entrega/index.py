# # Función para cargar usuarios desde JSON
# import json

# def cargar_usuarios():
#     with open ('usuarios.json', 'r') as archivo:
#         return json.load(archivo)
        
# # Función para guardar usuarios en un JSON
# def guardar_usuarios(usuarios):
#     with open("usuarios.json", "w") as archivo:
#         json.dump(usuarios, archivo)
    
# # Diccionario para almacenar usuarios y contraseñas
# usuarios = cargar_usuarios()

# # Funcion Registrar Usuario
# def registrar_usuario(usuarios):
#     nombre = input("Ingrese su nombre de usuario: ")
#     contrasena = input("Ingrese su contraseña: ")
#     usuarios[nombre] = contrasena   #agrega los datos al diccionario
#     guardar_usuarios(usuarios) # Guarda el diccionario en el archivo JSON
#     return print("Usuario registrado con éxito.")
    
    
# # Funcion para loguearse
# def loguearse(usuarios):
#     while True:
#         nombre = input("Ingrese su nombre de usuario: ").lower()
#         contrasena = input("Ingrese su contraseña: ").lower()
            
    
# # Validacion de datos del usuario


#         if nombre in usuarios and usuarios[nombre] == contrasena:  
#             print("Sesión Activa")
#             break
#         else:
#             print("Verifique su usuario o contraseña.")
#             intentar_nuevamente = input("¿Desea intentar nuevamente? SI/NO: ")
#             if intentar_nuevamente.upper() == "NO":
#                 break 



# # Función para mostrar usuarios registrados
# def ver_usuarios(usuarios):
#     print("Usuarios registrados:")
#     for nombre, contrasena in usuarios.items():
#         print(f"Usuario: {nombre} - Contraseña: {contrasena}")
        
        



# # Menu Principal
# menu_principal = True
# while menu_principal:
#     try:
#         opcion= int(input('Bienvenido! ¿Qué quieres hacer?\n 1-Loguearme \n 2-Registrarme \n 3-Mostrar Usuarios Registrados\n 4-Salir\n'))
#         if opcion == 1: 
#             loguearse(usuarios)
#         elif opcion == 2: 
#             registrar_usuario(usuarios)
#         elif opcion ==3:
#             ver_usuarios(usuarios)
#         elif opcion == 4:
#             guardar_usuarios(usuarios)
#             print("Hasta Pronto!")
#             menu_principal = False
#         else: 
#             print("Eliga una opción válida")
#     except:
#         print("Ocurrió un error.")