numero1 = int(input("digite el primer numero "))
numero2 = int(input("digite el segundo numero "))
numero3 = int(input("digite el tercer numero "))

if numero1<numero2 and numero1<numero3:
    print(f"el numero mas pequeño es {numero1}")
elif numero2<numero3 and numero2<numero1:
    print(f"el numero mas pequeño es {numero2}")
else:
    print(f"el numero mas pequeño es el {numero3}")

    
