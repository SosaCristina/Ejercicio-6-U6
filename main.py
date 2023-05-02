from ClaseViajeroFrecuente import Viajero
from ManejadorViajerosFrecuentes import Manejador
import csv



if __name__=='__main__':
    objeto=Manejador()
    objeto.TestLista()
    print(objeto)
    print("COMPARAR VIAJEROS")
    valor=int(objeto.comparar())
    objeto.mayor(valor)
    print("ACUMULAR MILLAS")
    num=int(input("Ingrese numero de viajero que desee acumular millas"))      
    indice=objeto.buscar(num)
    objeto.acumular(indice)
    print("CANJEAR MILLAS")
    num1=int(input("Ingrese numero de viajero que desee canjear millas"))
    indice=objeto.buscar(num1)
    objeto.canjear(indice)




