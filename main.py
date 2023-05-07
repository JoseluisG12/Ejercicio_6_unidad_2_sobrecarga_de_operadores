from ManejadorViajeros import ManejadorViajeros
from claseViajero import Viajero

def test():
    opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))
    while opc != 0:
        if opc == 1:
            viajero = Viajero(123,41230328,'gonzales','sergio',20000)
            viajero.mostrardatos()
            milla = int(input("ingrese la cantidad de millas a acumular\n"))
            viajero.AcumularMillas(milla)
            viajero.mostrardatos()
            milla = int(input("ingrese la cantidad de millas a canjear\n"))
            viajero.CanjearMillas(milla)
            viajero.mostrardatos()


        if opc == 2:
            viajero = Viajero(123, 41230328, 'gonzales', 'sergio', '2000km')
            viajero.mostrardatos()
            milla = int(input("ingrese la cantidad de millas a acumular\n"))
            viajero.AcumularMillas(milla)
            viajero.mostrardatos()
            milla = int(input("ingrese la cantidad de millas a canjear\n"))
            viajero.CanjearMillas(milla)
            viajero.mostrardatos()
        opc = int(input("desea probar el test 1 = datos correctos 2 = datos incorrectos 0 = salir\n"))


if __name__ == '__main__':
    opc = input("desea probar los metodos con la funcion test y = si n = no\n")
    if opc == 'y':
        test()
    print("_______main________")
    viajeros = ManejadorViajeros()
    viajeros.cargarDatos()
    viajeros.menu()