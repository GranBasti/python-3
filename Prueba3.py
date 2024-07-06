import json

# Lista
pedidos = []

def validar(mensaje, tipo_dato):
    
#Solicitar entrada al usuario y valida que no esté vacía. 
    while True:
        entrada = input(mensaje)
        if entrada.strip():  # Verifica que no sea una cadena vacía
            try:
                return tipo_dato(entrada)
            except ValueError:
                print("Error: Ingresa un valor válido.")
        else:
            print("Error: Este campo es obligatorio.")

#Solicitar información al usuario
def registrar_pedido():
    nombre_cliente = validar("Nombre y apellido del cliente: ", str)
    numero_contacto = validar("Número de contacto: ", str)
    tipo_evento = validar("Tipo de evento (corporativo o privado): ", str)
    fecha_evento = validar("Fecha del evento: ", str)
    direccion_evento = validar("Dirección del evento: ", str)
    menu_seleccionado = validar("Menú seleccionado (Comida Italiana, Comida Japonesa o BBQ): ", str)
    cantidad_comensales = validar("Cantidad de comensales: ", int)

#Diccionario con detalles del pedido
    pedido = {
        "Cliente": {
            "Nombre": nombre_cliente,
            "Contacto": numero_contacto
        },
        "Evento": {
            "Tipo": tipo_evento,
            "Fecha": fecha_evento,
            "Dirección": direccion_evento
        },
        "Menú": {
            "Seleccionado": menu_seleccionado,
            "Comensales": cantidad_comensales
        }
    }

#Agregar el pedido a la lista
    pedidos.append(pedido)
    print("Pedido registrado exitosamente.")

#Listar los pedidos
def listar_pedidos():
    print("\nLista de Pedidos:")
    for i, pedido in enumerate(pedidos, start=1):
        print(f"\nPedido {i}:")
        for categoria, detalles in pedido.items():
            print(f"{categoria}:")
            for campo, valor in detalles.items():
                print(f"  {campo}: {valor}")

#Generar TXT y JSON
def imprimir_detalle_por_menu():
    menu_elegido = input("\nSelecciona un menú (Comida Italiana, Comida Japonesa o BBQ): ")
    pedidos_menu = [pedido for pedido in pedidos if pedido['Menú']['Seleccionado'] == menu_elegido]

    if pedidos_menu:
        # Generar archivo .txt
        with open(f"pedidos_{menu_elegido.lower()}.txt", "w") as txt_file:
            for pedido in pedidos_menu:
                txt_file.write(json.dumps(pedido, indent=4))
                txt_file.write("\n\n")

        # Generar archivo .json
        with open(f"pedidos_{menu_elegido.lower()}.json", "w") as json_file:
            json.dump(pedidos_menu, json_file, indent=4)
        print(f"Archivos generados para el menú '{menu_elegido}'.")

    else:
        print(f"No hay pedidos registrados para el menú '{menu_elegido}'.")

# Ejecutar el programa
while True:
    print("\n--- Sistema de Gestión de Pedidos ---")
    print("1. Registrar Pedido")
    print("2. Listar Pedidos")
    print("3. Imprimir Detalle de Pedidos por Menú")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_pedido()
    elif opcion == "2":
        listar_pedidos()
    elif opcion == "3":
        imprimir_detalle_por_menu()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida")