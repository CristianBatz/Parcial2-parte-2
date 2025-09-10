class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedidos(Cliente):
    def __init__(self,nombre,producto,cantidad,prioridad):
        super().__init__(nombre)
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, producto: {self.producto}, cantidad: {self.cantidad}")

class GestionPedido(Pedidos):
    def __init__(self):
        self.Registrar_pedido = {}

    def agregar_pedido(self):
        print("=== Registrar pedido ===")
        codigo = input("Digite el código del pedido: ")
        nombre = input("Digite el nombre del cliente: ")
        producto = input("Digite el producto del pedido: ")
        cantidad = input("Digite la cantidad del pedido: ")
        prioridad = input("Digite la prioridad del pedido (urgente/normal): ")

        pedido = Pedidos(nombre,producto,cantidad,prioridad)

        self.Registrar_pedido[codigo] = pedido

        pedido.mostrar_info()

        if prioridad.lower() == "Urgente":
            NotificacionPedidoUrgente.notificar(nombre, producto)

    def buscar_pedido(self):
        print("=== Buscando pedido ===")
        codigo = input("Digite el código del pedido a buscar: ")
        if codigo in self.Registrar_pedido:
            print(f"Pedido encontrado:")
            self.Registrar_pedido[codigo].mostrar_info()
        else:
            print(" Pedido no encontrado.")

    def mostrar_info(self):
        if not self.Registrar_pedido:
            print("Pedido no encontrado.")
        else:
            for codigo,pedido in self.Registrar_pedido.items():
                print(f"codigo: {codigo}")
                pedido.mostrar_info()

class GuardarPedido:
    pass


class NotificacionPedidoUrgente(GestionPedido):

    def notificar(self,codigo):
        pass


class Busqueda:
    def guardar_pedido(self):
        with open("pedidos.log","w",encoding="utf-8") as f:
            pass



class Menu:
    def menu_mostrar(self):
        print("===Gestion Pedidos====")
        print("1. Agregar pedido")
        print("2. Buscar pedido")
        print("3. Mostrar pedidos")
        print("4. Salir")


menu = Menu()
gestion_pedidos = GestionPedido()
opcion = 0
while opcion != 4:

    menu.menu_mostrar()
    opcion = int(input("Seleccione una opcion: "))
    match int(opcion):
        case 1:
            gestion_pedidos.agregar_pedido()
        case 2:
            gestion_pedidos.buscar_pedido()
        case 3:
            print("Pedidos registrados:")
            for codigo, datos in gestion_pedidos.Registrar_pedido.items():
                print(f"codigo: {codigo}")
                datos.mostrar_info()
        case 4:
            print("Saliendo del programa")
        case _:
            print("Opcion no valida")





            def mostrar_todos(self):
                if not self.Registrar_pedido:
                    print("No hay pedidos registrados.")
                else:
                    for codigo, pedido in self.Registrar_pedido.items():
                        print(f"\nCódigo: {codigo}")
                        pedido.mostrar_info()


            def guardar_en_archivo(self, nombre_archivo="pedidos.txt"):
                GuardarPedido.guardar(self.Registrar_pedido, nombre_archivo)


    class GuardarPedido:
        @staticmethod
        def guardar(pedidos, nombre_archivo):
            with open(nombre_archivo, "w") as f:
                for codigo, pedido in pedidos.items():
                    f.write(f"{codigo},{pedido.nombre},{pedido.producto},{pedido.cantidad},{pedido.prioridad}\n")
            print(f"✅ Pedidos guardados en {nombre_archivo}")


    class NotificacionPedidoUrgente:
        @staticmethod
        def notificar(nombre, producto):
            print(f"🚨 ¡Atención! El cliente {nombre} ha realizado un pedido urgente del producto '{producto}'.")










