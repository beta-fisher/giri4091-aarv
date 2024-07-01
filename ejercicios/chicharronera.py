a = float (input("Ingresa el valor de a: ")) 
b = float (input("Ingresa el valor de b: ")) 
c = float (input("Ingresa el valor de c: "))

x1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(x1," ",x2)