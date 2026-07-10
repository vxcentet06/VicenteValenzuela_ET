recorridos = {
'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'dia', True],
'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'dia', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'dia', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'dia', True]

}

venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12]

}

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opc = int(input("Ingresa una opcion (1-6): "))
            if opc <= 1 or opc <= 6:
                return opc
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_origen(origen):
    return origen.strip() != ""

def validar_destino(destino):
    return destino.strip() != ""

def validar_dsitancia(distancia):
    return distancia > 0

def validar_tipo_bus(bus):
    return bus.lower() in ['normal','semi-cama','cama']

def validar_turno(turno):
    return turno.lower() in ['dia','noche']

def tiene_wifi(wifi):
    return wifi.lower() in ['s','n']

def validar_precio(precio):
    return precio > 0

def validar_asientos(asientos):
    return asientos > 0


def asientos_origen(origen, recorridos, venta):
    total = 0
    for codigo in recorridos:
        if recorridos[codigo][1].lower() == origen.lower():
            total += venta[codigo][1]
    print(f"El total de asientos disponibles es: {total}")



def busqueda_precio(recorridos, asientos, p_min, p_max):
    encontrados = []
    for codigo in recorridos:
        precio = recorridos[codigo][0]
        asientos = recorridos[codigo][1]
        if p_min <= precio <= p_max and asientos != 0:
            nombre = recorridos[codigo][0]
            encontrados.append(f"{nombre}----{codigo}")
    encontrados.sort()
    if not encontrados:
        print("No hay asientos por ese rango de precio")

def buscar_codigo(codigo, recorridos):
    for clave in recorridos:
        if clave.lower() == codigo.lower():
            return True
        return False

            
def main():
    while True:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            c = input("Ingrese ciudad de origen a consultar: ")
            asientos_origen(c, recorridos, venta)
        
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        break
                    else:
                        print("")
                except:
                    print("error")
            busqueda_precio(p_min,p_max,recorridos,venta)

        #elif opcion == 3:


        
        elif opcion == 6:
            print("Programa finalizado")
            break
        else:
            print("Ingrese una opcion valida")

main()