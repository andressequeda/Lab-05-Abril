num_u = int(input("Ingrese un digito: "))
if num_u % 5 == 0 and num_u % 3 == 0:
    print("El numero ingresado es multiplo de 5 y 3")
elif num_u % 5 == 0:
    print("El numero es multiplo de 5")
elif num_u % 3 == 0:
    print("El numero es multiplo de 3")
else:
    print("El numero ingresado no es multiplo de 5 y 3")