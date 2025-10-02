import random
nombres = [ "Sofía", "Mateo", "Valentina", "Sebastián", "Isabella", "Alejandro",
            "Camila", "Santiago", "Luciana", "Nicolás", "Martina", "Benjamín", "Valeria",
            "Joaquín", "Victoria", "Gabriel", "Emilia", "Samuel", "Julieta", "Daniel", "Antonella",
            "Diego", "Rafaela", "Felipe", "Mariana", "Emmanuel", "Catalina", "Lucas", "Agostina", "Andrés",
            "Constanza", "Ezequiel", "Bianca", "Ignacio", "Delfina", "Agustín", "Florencia", "Gastón",
            "Guadalupe", "Hernán", "Julia", "Javier", "Laura", "Leonardo", "Magdalena", "Martín", "Micaela",
            "Patricio", "Paulina", "Ramiro" ]
apellidos = [ "García", "Rodríguez", "González", "Fernández", "López", "Martínez",
              "Sánchez", "Pérez", "Gómez", "Martín", "Jiménez", "Ruiz", "Hernández", "Díaz",
              "Moreno", "Muñoz", "Álvarez", "Romero", "Alonso", "Gutiérrez", "Navarro", "Torres",
              "Domínguez", "Vázquez", "Ramos", "Gil", "Ramírez", "Serrano", "Blanco", "Molina", "Castro",
              "Suárez", "Ortega", "Rubio", "Delgado", "Morales", "Ortiz", "Marín", "Iglesias", "Núñez",
              "Medina", "Cortés", "Cano", "Flores", "Herrera", "Gallego", "Vega", "Castillo", "Santos",
              "Reyes" ]
clientes = []
for i in range(0, 10):
    cliente = {
        "id": i + 1,
        "nombre": nombres[i],
        "apellido": apellidos[i],
        "saldo": random.randint(500, 1500)
    }
    clientes.append(cliente)

def mostrar_clientes():
    for c in clientes:
        print(f"ID:{c['id']} - {c['nombre']} {c['apellido']} - Saldo:${c['saldo']}")

def buscar_cliente():
    seguimos = True
    while seguimos:
        try:
            opc = int(input("Ingrese algunos de los ID que se encuentran: "))
            for c in clientes:
                if c["id"] == opc:
                    print(f"Cliente encontrado: {c['nombre']} {c['apellido']} - Saldo:${c['saldo']}")
                    seguimos = False
                    return
                else:
                    print("El cliente no ha sido encontrado.")
        except (ValueError, KeyError):
            print("Ha ingresado algo mal. Intente de nuevo.")

def depositar():
    seguimos = True
    while seguimos:
        try:
            opc = int(input("Ingrese cuanto quiere depositar: "))
            if opc < 0:
                print("No puede ingresar un numero negativo. Intente de nuevo.")
            else:
                for c in clientes:
                    c["saldo"] += opc
                    print(f"Nuevo saldo de {c['nombre']}: ${c['saldo']}")
                    seguimos = False
                    return
        except (ValueError, KeyError, ):
            print("Ha ingresado algo mal. Intente de nuevo.")

def retirar():
    seguimos = True
    while seguimos:
        try:
            opc = int(input("Ingrese cuanto quiere retirar: "))
            for c in clientes:
                if opc > c["saldo"]:
                    print("No puede ingresar un numero mayor a su saldo. Intente de nuevo.")
                else:
                    for c in clientes:
                        c["saldo"] -= opc
                        print(f"Nuevo saldo de {c['nombre']}: ${c['saldo']}")
                        seguimos = False
                    else:
                        print("Saldo insuficiente.")
                return
        except (ValueError, KeyError):
            print("Ha ingresado algo mal. Intente de nuevo.")

print("LISTA INICIAL DE CLIENTES:")
mostrar_clientes()

print("BUSCAR CLIENTE POR ID:")
buscar_cliente()

print("DEPOSITAR:")
depositar()

print("RETIRAR:")
retirar()

print("LISTA FINAL DE CLIENTES:")
mostrar_clientes()