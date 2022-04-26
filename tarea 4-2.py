#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

lista=[]

for  num  in range (1,101):
   lista.append(num)
   listaR=lista[::-1]
print("Lista orden Normal")
print(lista, end=" ")
print("")
print("")
print("Lista orden inverso")

print(listaR, end=" ")
    
  
   
