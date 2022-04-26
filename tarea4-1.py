print("Calcular los numeros impares de un Rango de numeros dado")
inicio = int(input("Ingrese el # de inicio: "))
fin= int(input("Ingrese el # final: "))

for num in range (inicio, fin +1):
    if num % 2 !=0:
        print(num, end=" ")
