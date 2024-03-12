class Product():
    def __init__(self, id, name, desc, quantity, price):
        self.id = id
        self.name = name
        self.desc = desc
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"|ID: {self.id}|Nombre: {self.name}|Descripción: {self.desc}|Cantidad: {self.quantity}|Precio: ${self.price}"
    def update_name(self, nuevo_nombre):
        self.name = nuevo_nombre
        
    def update_desc(self, nueva_descripcion):
        self.desc = nueva_descripcion
        
    def update_quantity(self, nueva_cantidad):
        self.quantity = nueva_cantidad
        
    def update_price(self, nuevo_precio):
        self.price = nuevo_precio


