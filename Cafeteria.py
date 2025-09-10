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
    def __init__(self,codigo):
        self.codigo = codigo
        self.Registrar_pedido = {}

    def agregar_pedido(self):
        print("=== Registro de pedidos ===")
        nombre = input("Nombre del cliente: ")
        codigo = input("Digite el codigo del pedido: ")
        producto = input("Digite el producto del pedido: ")
        cantidad = input("Digite la cantidad del pedido: ")
        prioridad = input("Digite la prioridad del pedido: ")

        pedido = Pedido(nombre,producto,cantidad,prioridad)
        self.Registrar_pedido[codigo] = pedido

        self.nombre = nombre
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad

        self.Registrar_pedido[codigo] = {
            "nombre": nombre,
            "producto": producto,
            "cantidad": cantidad,
            "prioridad": prioridad
        }

        self.mostrar_info()

class GuardarPedido:
    pass

class NotificacionPedidoUrgente(GestionPedido):
    def __init__(self,codigo,nombre,producto,cantidad,prioridad):
        super().__init__(codigo,nombre,producto,cantidad,prioridad)


class Busqueda:
    pass


class Menu:
    def menu_mostrar(self):
        print("===Gestion Pedidos====")
        print("1. Agregar pedido")
        print("2. Buscar pedido")
        print("3. Mostrar pedidos")
        print("4. Salir")


menu = Menu()
gestion_pedidos = GestionPedido("000","","","","")
opcion = 0
while opcion != 4:

    menu.menu_mostrar()
    opcion = int(input("Seleccione una opcion: "))
    match int(opcion):
        case 1:
            gestion_pedidos.agregar_pedido()
        case 2:
            pass
        case 3:
            print("Pedidos registrados:")
            for codigo, datos in gestion_pedidos.Registrar_pedido.items():
                print(f"Código: {codigo}, nombre: {datos['nombre']}, Producto: {datos['producto']}, cantidad: {datos['cantidad']}, prioridad: {datos['prioridad']}")
        case 4:
            print("Saliendo del programa")
        case _:
            print("Opcion no valida")









