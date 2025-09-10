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

class GestionPedido():
    def __init__(self):
        self.Registrar_pedido = {}

    def agregar_pedido(self):
        print("=== Registrar pedido ===")
        codigo = input("Código del pedido: ")
        nombre = input("Nombre del cliente: ")
        producto = input("Producto: ")
        cantidad = input("Cantidad: ")
        prioridad = input("Prioridad (urgente/normal): ").lower()

        self.Registrar_pedido[codigo] = {
            "nombre": nombre,
            "producto": producto,
            "cantidad": cantidad,
            "prioridad": prioridad
        }

        self.mostrar_infoA()

        if prioridad == "urgente":
            NotificacionPedidoUrgente.notificar(nombre, codigo)

    def buscar_pedido(self):
        print("=== Buscando pedido ===")
        codigo = input("Digite el código del pedido a buscar: ")
        if codigo in self.Registrar_pedido:
            print(f"Pedido encontrado:")
            self.Registrar_pedido[codigo].mostrar_info()
        else:
            print(" Pedido no encontrado.")

    def mostrar_infoA(self):
        if not self.Registrar_pedido:
            print("Pedido no encontrado.")
        else:
            for codigo,pedido in self.Registrar_pedido.items():
                print(f"codigo: {codigo}")
                pedido.mostrar_info()

class GestionArchivosTextos:
    try:
        def cargar_datos(self):
            with open("pedido.log", "w",encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        codigo,nombre,producto,cantidad,prioridad = linea.split(",")
                        self.Registrar_pedido[codigo] = {
                            "nombre": nombre,
                            "producto": producto,
                            "cantidad": cantidad,
                            "prioridad": prioridad
                            }
            print("Pedidos cargados")
    except FileNotFoundError:
        print("Archivo pedido.log no existe,se creara un al guardar")

class NotificacionPedidoUrgente():

    def notificar(self,nombre,codigo):
        print("=== Pedidos Urgente ===")
        print(f"Cliente: {nombre}, Código: {codigo}")

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
