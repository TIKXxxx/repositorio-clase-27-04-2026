email = input("Ingrese su correo electrónico: ").strip().lower()
if "@" in email:
    print(f"Correo electrónico ingresado: {email}")
else:
    print("Correo electrónico inválido.")