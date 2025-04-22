nombres_invitados = ["diomedes", "luis fonsi", "carlos vives", "maluma"]

nombre = input("digite el nombre para ver si esta invitado")

if nombre in nombres_invitados: 
    print("felicidades, esta en la lista")
else: 
    print("lo lamento, no esta en la lista")
