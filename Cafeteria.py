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

class GestionPedido:
    def __init__(self):
        self.registrar_pedidos = {}

    def agregar_pedido(self):
        print("=== Registrar pedido ===")
        codigo = input("Código del pedido: ")
        nombre = input("Nombre del cliente: ")
        producto = input("Producto: ")
        cantidad = input("Cantidad: ")
        prioridad = input("Prioridad (urgente/normal): ").lower()

        pedido = Pedidos(nombre, producto, cantidad, prioridad)
        self.registrar_pedidos[codigo] = pedido

        pedido.mostrar_info()

        if prioridad == "urgente":
            NotificacionPedidoUrgente.notificar(pedido, codigo)

    def buscar_pedido(self):
        print("=== Buscar pedido ===")
        codigo = input("Digite el código del pedido a buscar: ")
        pedido = self.registrar_pedidos.get(codigo)
        if pedido:
            print("Pedido encontrado:")
            pedido.mostrar_info()
        else:
            print("Pedido no encontrado.")

    def mostrar_infoA(self):
        if not self.registrar_pedidos:
            print("No hay pedidos registrados.")
        else:
            for codigo, pedido in self.registrar_pedidos.items():
                print(f"Código: {codigo}")
                pedido.mostrar_info()

class GestionArchivosTextos:
    def __init__(self, gestor_pedidos):
        self.gestor = gestor_pedidos

    def cargar_datos(self):
        try:
            with open("pedido.log", "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, producto, cantidad, prioridad = linea.split(",")
                        pedido = Pedidos(nombre, producto, cantidad, prioridad)
                        self.gestor.registrar_pedidos[codigo] = pedido
            print("Pedidos cargados correctamente.")
        except FileNotFoundError:
            print("Archivo 'pedido.log' no encontrado. Se creará al guardar.")

        def guardar_datos(self):
            with open("pedido.log", "w", encoding="utf-8") as f:
                for codigo,pedido in self.gestor.registrar_pedidos.items():
                    linea = f"{codigo}, {pedido.nombre}, {pedido.cantidad}, {pedido.prioridad}\n"
                    f.write(linea)
            print("Pedidos guardados en archivo.")

class NotificacionPedidoUrgente():
    def notificar(self,pedido,codigo):
        if pedido.prioridad == "urgente":
            print("=== Notificación: Pedido Urgente ===")
            print(f"Código: {codigo}")
            pedido.mostrar_info()

class Menu:
    def menu_mostrar(self):
        print("===Gestion Pedidos====")
        print("1. Agregar pedido")
        print("2. Buscar pedido")
        print("3. Mostrar pedidos")
        print("4. Salir")


gestion_pedidos = GestionPedido()
archivo = GestionArchivosTextos(gestion_pedidos)
archivo.cargar_datos()
menu = Menu()
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
            gestion_pedidos.mostrar_infoA()
        case 4:
            print("Saliendo del programa")
        case _:
            print("Opcion no valida")
