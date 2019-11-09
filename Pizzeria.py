#!/usr/bin/env python
# -*- coding: utf-8 -*-
#enconding: utf-8

#Esta función es para realizar una simple suma.
suma = lambda x,y: x + y

#Esta función es para realizar una simple resta.
resta = lambda x,y: x - y

#Esta función es para preguntar si se desea cerrar la tienda o no. 
def nuevoCliente():
    #Llamada a variables globales
    global pizzas, ingredientes, precios, precioTotal,numPiz
    pizzas = []
    ingredientes = []
    precios = []
    precioTotal = 0
    numPiz = 0
    resp = input("Desea cerrar la tienda [s/n]: ")
    if (resp == "s"):
        exit()
    elif (resp == "n"):
        start()
    else:
        print("=> Debe seleccionar una opcion correcta!!")
        nuevoCliente()


#Esta función es para cancelar la compra.
def cancelarPedido():
    global pizzas, ingredientes, precios, precioTotal,numPiz
    pizzas = []
    ingredientes = []
    precios = []
    precioTotal = 0
    numPiz = 0
    print("\nHasta pronto, espero la proxima si pueda concretar el pedido\n")
    nuevoCliente()

#Esta función es para eliminar todo el pedido y volver a comenzar.
def eliminarPedido():
    #Llamada a variables globales
    global pizzas, ingredientes, precios, precioTotal,numPiz
    pizzas = []
    ingredientes = []
    precios = []
    precioTotal = 0
    numPiz = 0
    print("Se volvera a tomar todo el pedido")
    ordenar()
    
#Esta función es para elegir cual de las pizzas desea eliminar el cliente.
def eliminarPizza():
    #Llamada a variables globales
    global numPiz, pizzas, ingredientes, precios, precioTotal
    print("")
    #Imprime cada una de las pizzas ordenadas.
    for i in range(0,numPiz):
        monto = str(precios[i])
        ingre = str(ingredientes[i]).strip('[]')
        num = str(i+1)
        print(num + "-Pizza " + pizzas[i] + " " + ingre + " " + monto)
    numero = int(num) + 1
    num = str(numero)    
    print(num + "-Volver")
    resp = input("\nSelecciona la pizza que desea eliminar: ")
    print("")
    num = int(resp)
    if (num - 1 == len(pizzas)):
        masOpciones()
    elif (num > len(pizzas)):
        print("=> Debe seleccionar una opcion correcta!!")
        eliminarPizza()
    else:
        if (num > 0):
            pizzas.pop(num-1)
            ingredientes.pop(num-1)
            precioTotal = precioTotal - precios[num-1]
            precios.pop(num-1)
            numPiz = resta(numPiz,1) #Alternativa de numPiz = numPiz - 1
            nuevaCompra()

#Esta función es para ver la información relacionada con la orden.
def detalle():
    #Llamada a variables globales
    global numPiz, pizzas, ingredientes, precios,precioTotal
    total = str(precioTotal)
    if(len(pizzas) == 0):
        print("\nNo hay pedidos")
    else:
        print("")
        print("*********************************************")
        print("              Pizzeria Ucab                 \n")
        print("Pedidos:\n")
        #Imprime cada una de las pizzas ordenadas.
        for i in range(0,numPiz):
            monto = str(precios[i])
            ingre = str(ingredientes[i]).strip('[]')
            num = str(i+1)
            if (ingre == ""):
                print(num + "-Pizza " + pizzas[i] + " Margarita " + monto)
            else:
                print(num + "-Pizza " + pizzas[i] + " con " + ingre + " " + monto)
        print("\nMonto total: " + total)
        print("*********************************************")
    nuevaCompra()

#Esta función es para indicar cuál de las funcionalidades adicionales se desea seleccionar.
def masOpciones():
    print("Ver pedido (v)\nEliminar pizza (p)\nEliminar pedido (z)\nCancelar compra (c)\nVolver (a)\n")
    resp = input("Indique una opcion: ")
    if (resp == "v"):
        detalle()
    elif (resp == "p"):
        eliminarPizza()
    elif (resp == "z"):
        eliminarPedido()
    elif (resp == "c"):
        cancelarPedido()
    elif (resp == "a"):
        nuevaCompra()
    else:
        print("=> Debe seleccionar una opcion correcta!!\n") 
        masOpciones()
    
#Esta función es para indicar si quieres continuar comprando, terminar la compra o ver las opciones adicionales.
def nuevaCompra():
    #Llamada a variables globales
    global numPiz, precioTotal
    num = str(numPiz)
    monto = str(precioTotal)
    print("\n**************************")
    resp = input("¿Desea continuar [s/n]? (preciona x para mas opciones): ")
    print("**************************\n")
    if (resp == "s"):
        ordenar()
    elif (resp == "n"):
        print("Su pedido tiene un total de " + num + " pizza(s) por un monto de " + monto)
        print("\nGracias por su compra, regrese pronto\n")
        nuevoCliente()
    elif (resp == "x"):
        masOpciones()
    else:
        print("\n=> Debe seleccionar una opcion correcta!!") 
        nuevaCompra()

#Esta función es para indicar información de cada pizza luego de ordenarla (Tamaño de la pizza, ingredientes que contiene y precio).
def finalizandoPedido():
    #Llamada a variables globales
    global pizzas, numPiz, ingredientes,precios
    monto = str(precios[numPiz-1])
    ingre = str(ingredientes[numPiz-1]).strip('[]')
    if (ingre == ""):
        print("\nUsted selecciono una pizza "+ pizzas[numPiz-1] + " Margarita")
    else:
        print("\nUsted selecciono una pizza "+ pizzas[numPiz-1] + " con: " + ingre)
    print("\nSubtotal por pizza " + pizzas[numPiz-1] + ": " + monto)
    nuevaCompra()

#Esta función es para indicar que ingredientes se pueden agregar o no a la pizza.
def ingrediente():
    #Llamada a variables globales
    global ingredientesIn,precioTotal,monto,precios
    aditional = input("Indique el ingrediente (enter para terminar): ")
    if(aditional == "ja"):
        ingredientesIn.append("Jamon")
        precioTotal = suma(precioTotal,40) #Alternativa de precioTotal = precioTotal + 40
        monto = suma(monto,40) #Alternativa de monto = monto + 40
    elif (aditional == "ch"):
        ingredientesIn.append("Champinones")
        precioTotal = suma(precioTotal,35) #Alternativa de precioTotal = precioTotal + 35
        monto = suma(monto,35) #Alternativa de monto = monto + 35
    elif (aditional == "pi"):
        ingredientesIn.append("Pimenton")
        precioTotal = suma(precioTotal,30) #Alternativa de precioTotal = precioTotal + 30
        monto = suma(monto,30) #Alternativa de monto = monto + 30
    elif (aditional == "dq"):
        ingredientesIn.append("Doble queso")
        precioTotal = suma(precioTotal,40) #Alternativa de precioTotal = precioTotal + 40
        monto = suma(monto,40) #Alternativa de monto = monto + 40
    elif (aditional == "ac"):
        ingredientesIn.append("Aceitunas")
        precioTotal = suma(precioTotal,58) #Alternativa de precioTotal = precioTotal + 58
        monto = suma(monto,58) #Alternativa de monto = monto + 58
    elif (aditional == "pp"):
        ingredientesIn.append("Peperoni")
        precioTotal = suma(precioTotal,38.5) #Alternativa de precioTotal = precioTotal + 38.5
        monto = suma(monto,38.5) #Alternativa de monto = monto + 38.5
    elif (aditional == "sa"):
        ingredientesIn.append("Salchichon")
        precioTotal = suma(precioTotal,62.5) #Alternativa de precioTotal = precioTotal + 62.5
        monto = suma(monto,62.5) #Alternativa de monto = monto + 62.5
    elif (aditional == ""):
        ingredientes.append(ingredientesIn)
        precios.append(monto)
        monto = 0
        ingredientesIn = []
        finalizandoPedido()
    else:
        print("\n=> Debe seleccionar un ingrediente correcto!!\n")
        ingrediente()
    ingrediente()

#Esta función es para indicar el tamaño de la(s) pizza(s) a ordenar.      
def tamano():
    #Llamada a variables globales
    global pizzas,precio,precioTotal, monto
    size = input("Tamaño: Grande (g), Mediana (m), Pequeña (p): ")
    if (( size == "g" ) or ( size == "m" ) or ( size == "p" )):
        if (size == "g"):
            print("\nTamaño seleccionado: Grande")
            precio = suma(precio,580) #Alternativa de precio = precio + 580
            monto = suma(monto,580) #Alternativa de monto = monto + 580
            pizzas.append("Grande")
        elif (size == "m"):
            print("\nTamaño seleccionado: Mediana")
            precio = suma(precio,430) #Alternativa de precio = precio + 430
            monto = suma(monto,430) #Alternativa de monto = monto + 430
            pizzas.append("Mediana")
        else:
            print("\nTamaño seleccionado: Pequeña")
            precio = suma(precio,280) #Alternativa de precio = precio + 280
            monto = suma(monto,280) #Alternativa de monto = monto + 280
            pizzas.append("Pequeña")
        precioTotal = suma(precioTotal,precio) #Alternativa de precioTotal = precioTotal + precio
        precio = 0
        print("\nIngredientes:\n")
        print(" Jamon (ja)\n Champiñones (ch)\n Pimenton (pi)\n Doble queso (dq)\n Aceitunas (ac)\n Peperoni (pp)\n Salchichon (sa)\n")
        ingrediente()
    else:
        print("=> Debe seleccionar el tamano correcto!!")
        tamano()

#Esta función indica el número actual de la pizza que se va a ordenar y llama a la función tamano.
def ordenar():
    #Llamada a variables globales
    global numPiz
    numPiz = suma(numPiz,1) #Alternativa de numPiz = numPiz + 1
    num = str(numPiz)
    print("Pizza numero " + num)
    print("\nOpciones:\n")
    tamano()

#Esta función sólo imprime el encabezado de la aplicación.
def start():
    print("\n*****************")
    print("* Pizzeria Ucab *")
    print("*****************\n")
    ordenar()

#Variables Globales    
numPiz = 0
pizzas = []
ingredientes = []
ingredientesIn = []
monto = 0
precios = []
precio = 0
precioTotal = 0

start()
