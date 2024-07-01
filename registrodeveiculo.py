import os 
os.system("cls")

titulo = f"""{"Listado de datos de vehiculos"}
{"costo":<20}{"marca":<20}{"año":<15}{"kilo":10}{"reparacion":<10}{"costo total":<10}"""
pedido = []
marcas = ["toyota","ferrari","susuki"]
menu = """
1. Registrar Vehiculo 
2. Lista todos los Vehiculos Registrados 
3. Imprimir Orden de Reparacion 
4. Salir
"""
def registrar_vehiculo():
    while True:
        marca = input(f"marcas {marcas}: ").strip().lower()
        año = int(input("año de fabricacion: "))
        kilo = int(input("Kilometraje: "))
        costo = int(input("costo de reparacion: "))
        reparacion = round(costo * 0.08)
        costototalalpagar = round(costo + reparacion)
        pedido.append[marca, año, kilo, costo, reparacion, costototalalpagar]
        print(f"vehiculo registrado con exito")
        print(f"marca: {marca} año: {año} kilometraje: {kilo} costo de reparacion: {costo} reparacion: {reparacion} costo total: {costototalalpagar}")


def lista_todos_los_vehiculos_registrados():
    salida = titulo
    for t in pedido:
        salida += f"{t[0]:<20}"
        salida += f"{t[1]:<20}"
        salida += f"{t[2]:<15}"
        salida += f"{t[3]:<10}"
        salida += f"{t[4]:<10}"
        salida += f"{t[5]:<10}"
        salida += "\n"
    return salida
def imprimir_orden_de_reparacacion():
    imprimir = input(f"cargo por imprimir [todo/{marcas}]: ").strip().lower()
    if imprimir == "todo":
        with open("listado.txt", "w") as archivo:
            archivo.write(lista_todos_los_vehiculos_registrados())
    elif imprimir in marcas:
        with open(f"{imprimir}.txt", "w") as archivo:
            archivo.write(lista_todos_los_vehiculos_registrados())
    else:
        input("marca no encontrada")
while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1:
            registrar_vehiculo()
        elif opc == 2:
            print(lista_todos_los_vehiculos_registrados())
        elif opc == 3:
            imprimir_orden_de_reparacacion()
    except Exception as e:
        input(f"excepcion de menu {str(e)}")
