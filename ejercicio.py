class dojo:
    def __init__(self,x,y,s):
        self.menor=x
        self.mayor=y
        self.salto=s
        self.rango=range(menor, mayor,salto)
    def suma(self):
        suma=0
        for i in self.rango:
            suma+=i #
        print(suma)
        return suma
print ("ingrese menor")
menor=int(input())

print("ingrese mayor")
mayor=int(input())
print("ingrese salto")
salto=int(input())

calcular=dojo(menor,mayor,salto)

print(menor,mayor)

calcular.suma()
