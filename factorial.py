
factorial = 1 
a = int(input("Ingresa un numero " ))
b = 1
if a < 0:
    print ("El factorial es: ")
    print(factorial)
elif a == 0 :
    print ("El factorial es: ")
    print (factorial)
else :
    for b in range (1,a+1):
        factorial =  b * factorial 
    print("El factorial es: ")
    print(factorial)