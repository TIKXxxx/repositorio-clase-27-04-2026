edad = 10 #int
permiso = True#BooLean

if edad >= 18 and permiso:
    print("Puede salir")

elif edad >= 18 and not permiso:
    print("Debe pedir permiso")
else:
    print("Olvidese de salir")