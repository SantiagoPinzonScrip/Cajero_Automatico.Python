import os

def cargar_saldo():
    if not os.path.exists("saldo.txt"):
        with open("saldo.txt", "w") as f:
            f.write("1000.0")
        return 1000.0
    
    with open("saldo.txt", "r") as f:
        return float(f.read())

def guardar_saldo(nuevo_saldo):
    with open("saldo.txt", "w") as f:
        f.write(str(nuevo_saldo))
        
saldo = cargar_saldo()

def mostrar_menu():
    print("\n" + "="*25)
    print("    CAJERO AUTOMATICO")
    print("="*25)
    print("1. Consultar Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    print("="*25)

saldo = 1000.0

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(f"\n Su saldo actual es: ${saldo:.2f}")
    elif opcion == "2":
        try:
            monto = float(input("\n ¿Cuánto desea retirar?: "))
            if monto <= 0:
                print(" El monto debe ser mayor a cero.")
            elif monto > saldo:
                print(" Error: Fondos insuficientes.")
            else:
                saldo = saldo - monto
                print(f" ¡Retiro exitoso! Retire su dinero.")
                print(f"Saldo restante: ${saldo:.2f}")
        except ValueError:
            print(" Error: Por favor, ingrese un número válido.")
    elif opcion == "3":
        print("\n Gracias por usar nuestros servicios. ¡Buen día!")
        break 
    else:
        print("\n Opción no válida, intente de nuevo.")
