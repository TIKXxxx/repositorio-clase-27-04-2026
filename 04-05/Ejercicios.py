# Ejercicio 1 — Clasificador de Pasajero
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño: pasa gratis.")
elif edad < 17:
    print("Adolescente: tarifa media.")
elif edad < 65:
    print("Adulto: tarifa completa.")
else:
    print("Adulto mayor: tarifa media.") 

# Ejercicio 2 — Descuento en Tienda
precio_producto = float(input("Ingrese el precio del producto: "))
socio = input("¿Es usted socio del club de descuentos? (sí/no): ").lower()

if precio_producto > 50000 and socio == "sí":
    print("Tiene derecho a un descuento del 20%.")
    descuento = 0.20
elif precio_producto > 50000 and socio == "no":
    print("Tiene derecho a un descuento del 10%.")
    descuento = 0.10
elif precio_producto <= 50000 and socio == "sí":
    print("Tiene derecho a un descuento del 5.")
    descuento = 0.5
else:
    print("No tiene derecho a ningún descuento.")
    descuento = 0.0
    
final = precio_producto * (1 - descuento)
print(f"El precio final del producto es: {final:.2f}")

# Ejercicio 3 — Tarifa de Estacionamiento
horas = int(input("Ingrese la cantidad de horas: "))
tipo = input("Ingrese el tipo de vehículo (1:auto/2:moto/3:camion): ").lower()
base = 2000 * horas
total = 0

if horas > 12:
    print("Máximo 12 horas")
elif tipo == "1" or tipo == "auto" and horas > 3:
    total = base * 0.90
elif tipo == "2" or tipo == "moto" and horas > 3:
    total = base * 0.50
elif tipo == "3" or tipo == "camion" and horas > 3:
    total = base * 1.35
else:
    total = base
    
print(f"El total a pagar es: ${total:.0f}, con una cantidad de horas de: {horas} y un tipo de vehículo: {tipo}")

# Ejercicio 4 — Plan de Gimnasio
meses = int(input("Ingrese la cantidad de meses: "))
plan = input("Ingrese el tipo de plan (1: básico/2: estándar/3: premium): ").lower()
base = 30000 
insc = 10000

if meses >= 6 and plan == "1" or plan == "básico":
    descuento = 0.15
elif meses >= 6 and plan == "3" or plan == "premium":
    descuento = 0.25
elif meses == 3 or meses == 5 and plan == "1" or plan == "2" or plan == "3":
    descuento = 0.08
else:
    descuento = 0.0
mensual = base * (1 - descuento)

if meses >= 6 and (plan == "2" or plan == "3"):
    insc_final = 0
elif plan == "2" or plan == "3":
    insc_final = insc*0.50
else: insc_final = insc     

print(f"El costo mensual del plan es: ${mensual:.0f}, con una cantidad de meses de: {meses} y un tipo de plan: {plan}")
print(f"El costo de inscripción es: ${insc_final:.0f}")