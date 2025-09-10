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
    def __init__(self,codigo,producto,cantidad,prioridad):
        super().__init__(producto,prioridad,cantidad)
        self.codigo = codigo
        self.Registrar_pedido = {}

    def agregar_pedido(self):
        codigo = input("Digite el codigo del pedido: ")
        producto = input("Digite el producto del pedido: ")
        cantidad = input("Digite la cantidad del pedido: ")
        prioridad = input("Digite la prioridad del pedido: ")
        self.Registrar_pedido[codigo] = {
            "producto": producto,
            "cantidad": cantidad,
            "prioridad": prioridad
        }
        self.mostrar_info()

class GuardarPedido:
    pass



