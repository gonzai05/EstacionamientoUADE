import time
from time import sleep

lista_dni = [] #Lista con el dni de todos los clientes
facturacion_cliente = [] #Facturacion por cliente (Pago indivdual)
ingresos_cliente = [] #Ingresos totales por cliente
lista_precios = [0,1000,2000,2500,3500,4500,5000,6000,6500,7500,8500,9000,10000,11000,11500,12500,13500,14000,15000,16000,16500,17500,18500,19000,20000] #Lista con los precios por hora

print("Bienvenidos al estacionamiento UADE")
print("Cuadrilla de tarifas:")
time.sleep(0.5)

for i in range(len(lista_precios)):
    if i != 0:
        print(i,"Hora =", lista_precios[i])

dni = int(input("Introduzca su DNI:"))

lista_dni.append (dni)

c_horas = int(input("Ingrese la cantidad de horas deseada (1-24 horas): "))

facturacion_cliente.append(lista_precios[c_horas])
print("Dar ticket con:","DNI:",  lista_dni, "y el monto:",  facturacion_cliente)

print ('sale del estacionamiento ')