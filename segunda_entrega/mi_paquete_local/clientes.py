from personas import Persona

lista_de_clientes = []

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, genero, direccion, telefono, saldo):
        super().__init__(nombre, apellido, edad, genero)
        self._direccion = direccion
        self._telefono = telefono
        self._saldo = saldo
        
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nEdad: {self.edad}\nGénero: {self.genero}\nDirección: {self._direccion}\nTeléfono: {self._telefono}\nSaldo: ${self._saldo}"

      
def comprar(self):
    producto = input("¿Que desea comprar?")
    precio = 1000
    print(f"{producto} cuesta ${precio}")
    
    confirmar_compra = input("¿Desea comprar este producto? SI/NO: ")
    if confirmar_compra.upper() == "NO":
        print("Muchas gracias por su visita.")
        return
        
    # while True:
    #     if precio <= self._saldo:
    #         self._saldo -= precio
    #         print(f"Tu compra de {producto}ha sido realizada con éxito! Saldo restante: ${self._saldo}")
    #         break
    #     else:
    #         print("Saldo insuficiente para realizar la compra.")
    #         intentar_nuevamente = input("¿Desea intentar nuevamente? SI/NO: ")
    #         if intentar_nuevamente.upper() == "NO":
    #             break

def cancelar_compra():
        print('Tu compra ha sido cancelada')
        
        
def ingresar(lista_de_clientes):
    while True:
        nombre = input("Ingrese su nombre de cliente: ")
        saldo = float(input("Ingrese su saldo: "))

        for cliente in lista_de_clientes:
            if cliente['nombre'] == nombre and cliente['saldo'] == saldo:
                print("Sesión Activa")
                return 
            else:
                print("Verifique su nombre o saldo.")
                intentar_nuevamente = input("¿Desea intentar nuevamente? SI/NO: ")
                if intentar_nuevamente.upper() == "NO":
                    break
                
def registrar():
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        edad = int(input("Ingrese su edad: "))
        genero = input("Ingrese su género: ")
        direccion = input("Ingrese su dirección: ")
        telefono = int(input("Ingrese su teléfono: "))
        saldo = float(input("Ingrese su saldo: "))
        
        cliente = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "genero": genero,
        "direccion": direccion,
        "telefono": telefono,
        "saldo": saldo
    }
        cliente = Cliente(nombre, apellido, edad, genero, direccion, telefono, saldo)
        lista_de_clientes.append(cliente)
        print("Ha sido registrado con éxito.")
        print(cliente)
        

        
        

    
        