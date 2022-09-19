class calculadora:
    
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        
    def suma(self):
        print(self.a + self.b)

    def resta(self):
         print(self.a- self.b)

    def multiplicacion(self):
       print(self.a*self.b)

    def division(self):
        if (self.b == 0):
           print("No se puede dividir entre cero")
        else:
           print(self.a/self.b)
    

a = float(input("Ingresa el primer valor: "))
b=  float(input("Ingresa el segundo valor: "))

calculadora  = calculadora(a,b)
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()