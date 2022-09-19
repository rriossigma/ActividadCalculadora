def suma(a,b):
    print(a + b)

def resta(a,b):
    print(a- b)

def multiplicacion(a,b):
    print(a*b)

def division(a,b):
    if (b == 0):
        print("No se puede dividir entre cero")
    else:
        print(a/b)
    

a = float(input("Ingresa el primer valor: "))
b=  float(input("Ingresa el segundo valor: "))

suma(a,b)
resta(a,b)
multiplicacion(a,b)
division(a,b)