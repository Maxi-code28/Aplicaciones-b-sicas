def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir (a,b):
    return a / b

num1= int(input("ingrese un numero:"))
num2= int(input("ingrese otro numero:"))

print(f"suma:{sumar(num1,num2)}")
print(f"multiplica:{multiplicar(num1,num2)}")
print(f"divide:{dividir(num1,num2)}")