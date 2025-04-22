nombres = []

nombre = input("ingrese el nombre que desea agregar a la lista")

nombres.append(nombre)

respuesta = input("desea agregar otro nombre? (si/no)")

while respuesta =="si":
    nombre = input("ingrese el nombre que desea agregar a la lista")
    nombres.append(nombre)
    respuesta = input("desea agregar otro nombre? (si/no)")

for nombre in nombres:
    print(nombre)
    
   

        
    
        

