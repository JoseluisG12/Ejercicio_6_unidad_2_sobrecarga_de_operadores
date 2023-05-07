


class Viajero:
    __numero_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = ''

    def __init__(self,numero, dni, nombre, apellido, millas):
        self.__numero_viajero = int(numero)
        self.__dni = int(dni)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = int(millas)

    def getNombre(self):
        return self.__nombre
    def CantidaTotalMillas(self):
        return self.__millas_acum

    def AcumularMillas(self,millas):
        self.__millas_acum += millas
        return self.__millas_acum

    def CanjearMillas(self,millascanjear):
        if millascanjear <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - millascanjear
            return self.__millas_acum
        else:
            return None
    def mostrardatos(self):
        print('numero de viajero: {},dni: {},nombre: {},apellido: {},millas acumuladas: {}'.format(self.__numero_viajero,self.__dni,self.__apellido,self.__nombre,self.__millas_acum))
    def getnumero(self):
        return self.__numero_viajero

    def getmillas(self):
        return self.__millas_acum

    def __gt__(self,maxV):
        return self.__millas_acum > maxV

    def __str__(self):
        return 'el viajero {} posee la mayor cantidad de millas acumuladas:{}'.format(self.__nombre,self.__millas_acum)

    def __ne__(self,num):
        if self.__numero_viajero != num:
            return False
        else:
            return True

    def __add__(self,milla):
        return Viajero(self.__numero_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum + milla)

    def __sub__(self,milla):
        return Viajero(self.__numero_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum - milla)