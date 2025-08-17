#Creado por Felipe Bolivar
#Creado el 14/08/25

#Verificar si una matrícula de carro es par o impar (para pico y placa).

import os

print("¿Desea saber que dias no puede circular en su vehiculo?")
print("Primero indicame por favor los 3 numeros finales de tu placa")
placa = int(input("Digita tu respuesta: "))
print("Ahora indicame por favor el dia del mes ")
dia = int(input("Indica tu respuesta: "))
print("""Estas en un fin de semana o festivo
      [1] Si
      [2] No""")
opcion = int(input("Ingresa tu respuesta: "))
resultado1 = ""
resultado2 = ""
dia1 = ""
dia2 = ""

if opcion == 1:
    os.system("cls")
    print("Entonces no debes preocuparte por el pico y placa")
elif opcion == 2:
    if (placa % 2 == 0 and dia % 2 == 0) or (placa % 2 != 0 and dia % 2 != 0):
        print(f"Según el número de placa ingresado ({placa}), usted SI tiene pico y placa hoy.")
    else:
        print(f"Según el número de placa ingresado ({placa}), usted hoy NO tiene pico y placa.")
else:
    os.system("cls")
    print("Opcion incorrecta")  
