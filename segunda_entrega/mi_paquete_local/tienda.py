import clientes

menu_tienda = True
while menu_tienda:
        opcion= int(input('Bienvenido! ¿Qué quieres hacer?\n 1-Registrarme \n 2-Ingresar \n 3-Comprar\n 4-Cancelar compra\n 5-Salir\n'))
        if opcion == 1:
            clientes.registrar()
        elif opcion == 2: 
            clientes.ingresar()
        elif opcion == 3: 
            clientes.comprar()
        elif opcion == 4: 
            clientes.cancelar_compra()            
        elif opcion == 5:
            print("Gracias por visitarnos! Hasta Pronto!")
            menu_tienda = False
        else: 
            print("Eliga una opción válida")
        


