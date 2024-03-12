from producto import Product
from inventario import Inventory

def menu():
    inventory = Inventory()  

    while True:
        print("*************************************************")
        print("Bienvenido al Sistema de Gestión de Inventario")
        print("*************************************************")
        print("\n1. Agregar producto al inventario")
        print("2. Eliminar producto del inventario")
        print("3. Actualizar producto en el inventario")
        print("4. Buscar un producto en el inventario")
        print("5. Listar todos los productos en el inventario")
        print("6. Salir")

        option = input("\nPor favor, selecciona una opción: ")

        if option == "1":
            id = input("ID del producto: ")
            name = input("Nombre del producto: ")
            desc = input("Descripción del producto: ")
            try:
                quantity = int(input("Cantidad del producto: "))
                price = int(input("Precio del producto: "))
                product = Product(id, name, desc, quantity, price)
                inventory.add_product(product)
            except ValueError:
                print("Error: La cantidad y/o el precio deben ser números enteros.")

        elif option == "2":
            id = input("ID del producto a eliminar: ")
            inventory.delete_product(id)

        elif option == "3":
            id = input("ID del producto a actualizar: ")
            name = input("Nuevo nombre. 'Presiona ENTER para dejar igual' : ")
            desc = input("Nueva descripción. 'Presiona ENTER para dejar igual' : ")
            quantity = input("Nueva cantidad. 'Presiona ENTER para dejar igual' : ")
            price = input("Nuevo precio. 'Presiona ENTER para dejar igual' : ")
            inventory.update_product(id, name, desc, quantity, price)

        elif option == "4":
            id = input("ID del producto a buscar: ")
            inventory.find_product(id)

        elif option == "5":
            inventory.list_products()

        elif option == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


menu()
