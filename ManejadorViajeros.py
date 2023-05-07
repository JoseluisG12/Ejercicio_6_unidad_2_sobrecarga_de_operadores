from claseViajero import Viajero
import csv

class ManejadorViajeros():
    __viajeros = []

    def __init__(self):
        self.__viajeros = []
    def cargarDatos(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            numero = fila[0]
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas = fila[4]
            via = Viajero(numero, dni, nombre, apellido, millas)
            self.__viajeros.append(via)

        archivo.close()




    def menu(self):

        b = int(input("""
    Menu principal:
1-saber que viajero posee mas millas con sobrecaraga de operador >
2-acumular millas sobrecargando el operador +
3- para canjear millas sobrecargando el operador -
4-mostrar lista viajeros
0-salir\n"""))


        while b != 0:

            if b == 1:
                maxM = 0
                for i in range(len(self.__viajeros)):
                    if self.__viajeros[i] > maxM:
                        maxM = self.__viajeros[i].getmillas()
                        ind = i
                print(self.__viajeros[ind])

            if b == 2:
                num = int(input("ingrese el numero del viajero\n"))
                band = False
                i = 0
                while band != True:
                    band = self.__viajeros[i] != num
                    if band == False:
                        i+=1


                milla = int(input("ingrese la cantidad de millas a acumular\n"))
                self.__viajeros[i] = self.__viajeros[i] + milla

            if b == 3:
                num = int(input("ingrese el numero del viajero\n"))
                band = False
                i = 0
                while band != True:
                    band = self.__viajeros[i] != num
                    if band == False:
                        i += 1

                milla = int(input("ingrese la cantidad de millas a canjear\n"))
                self.__viajeros[i] = self.__viajeros[i] - milla
            if b == 4:

                for i in range(len(self.__viajeros)):
                    self.__viajeros[i].mostrardatos()

            b = int(input("""
    Menu principal:
1-saber que viajero posee mas millas con sobrecaraga de operador >
2-acumular millas sobrecargando el operador +
3- para canjear millas sobrecargando el operador -
4-mostrar lista viajeros
0-salir\n"""))

