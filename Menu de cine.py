import os
def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menu
    """
    os.system('clear') # NOTA para windows tienes que cambiar clear por cls
    print("Menú de cine")
    print("Selecciona una opción")
    print("\t1 - Pelicula 1")
    print("\t2 - Pelicula 2")
    print("\t3 - Pelicula 3")
    print("\t9 - salir")
def pelicula1():
        """ para presentar peliculas """
        print("La pelicula de 1 es: The Avengers End Game" )
def pelicula2():
        print("La pelicula 2 es: Terminator: Destino Oculto" )
def pelicula3():
        print("La pelicula 3 es: Aquaman")
        comida()
def comida():
        """ funcion para comidas"""
        print("quiere comida que individual cuesta $4.50" )
def comida2():
        print("quiere el combo duo que cuesta $7.50")
def comida3():
        print("quiere el combo familia que cuesta $12.50")
def horario():
        """ funcion de horarios de peliculas """
        print("Los horarios de la pelicula son : 10:30a.m, 1:30 p.m, 4.50p.m")

while True:
# Mostramos el menu
    menu()
# solicituamos una opción al usuario
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu=="1":
        print("")
        pelicula2()
        horario()
        comida()
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    elif opcionMenu=="2":
        print("")
        pelicula1()
        horario()
        comida2()
        input("Has escogido la opcion 2 ...\npulsa una tecla para continuar")
    elif opcionMenu=="3":
        print("")
        pelicula3()
        horario()
        comida3()
        
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionMenu=="9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")