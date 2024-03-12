class Inventory():
    def __init__(self):
        self.products = {}

    def add_product(self, producto):
        if producto.id in self.products:
            print("Error: Ya existe un producto con este ID.")
        else:
            self.products[producto.id] = producto
            print("\nProducto agregado exitosamente.\n")
    
    def delete_product(self, id):
        if id in self.products:
            del self.products[id]
            print("\nProducto eliminado exitosamente.\n")
        else:
            print("Error: No existe un producto con este ID.")
    
    def update_product(self, id, nombre=None, descripcion=None, cantidad=None, precio=None):
        if id in self.products:
            if nombre:
                self.products[id].update_name(nombre)
            if descripcion:
                self.products[id].update_desc(descripcion)
            if cantidad is not None:
                self.products[id].update_quantity(cantidad)
            if precio is not None:
                self.products[id].update_price(precio)
            print("\nProducto actualizado exitosamente.\n")
        else:
            print("Error: No existe un producto con este ID.")

    def find_product(self, id):
        if id in self.products:
            print(self.products[id])
        else:
            print("Producto no encontrado.")
    
    def list_products(self):
        if not self.products:
            print("El inventario está vacío.")
        else:
            print('Tienes estos productos en tu inventario:\n')
            for producto in self.products.values():
                print(producto)









