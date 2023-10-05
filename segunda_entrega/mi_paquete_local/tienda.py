import clientes


menu_tienda = True
while menu_tienda:
    opcion = int(input('Bienvenido! ¿Qué quieres hacer?\n 1-Registrarme \n 2-Ingresar \n 3-Comprar\n 4-Cancelar compra\n 5-Salir\n'))
    if opcion == 1:
        cliente = clientes.registrar()  #Instancio mi cliente para poder usar los metodos
    elif opcion == 2:
        cliente = clientes.ingresar()  
    elif opcion == 3:
        if cliente is not None:
            cliente.comprar()
        else:
            print("Debes ingresar o registrarte primero.")
    elif opcion == 4:
        cliente = clientes.cancelar_compra()
    elif opcion == 5:
        print("Gracias por visitarnos! Hasta Pronto!")
        menu_tienda = False
    else:
        print("Elige una opción válida")



