class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.hijos = []

#OPCION NUMERO 1
def Insertar_Izquierda(raiz, valor):
    if raiz is None:
        raiz = Nodo(valor)
    else:
        if raiz.izquierda is None:
            raiz.izquierda = Nodo(valor)
        else:
            Insertar_Izquierda(raiz.izquierda, valor)
    return raiz

def Insertar_Derecha(raiz, valor):
    if raiz is None:
        raiz = Nodo(valor)
    else:
        if raiz.derecha is None:
            raiz.derecha = Nodo(valor)
        else:
            Insertar_Derecha(raiz.derecha, valor)
    return raiz

#OPCION NUMERO 2
def Iniciar_Juego(raiz):
    nodo_actual = raiz

    while nodo_actual.izquierda or nodo_actual.derecha:
        respuesta = input(nodo_actual.valor + " (SI/NO): ")

        if respuesta.lower() == "si" or respuesta.upper() == "SI":
            nodo_actual = nodo_actual.izquierda

        else:
            nodo_actual = nodo_actual.derecha

    print("Es un(a) " + nodo_actual.valor + "? (SI/NO)")
    respuesta = input()

    if respuesta.lower() == "SI":
        print("¡FELICIDADES!")
        print("¡He Adivinado Correctamente!")

    else:
        print("¡LO LAMENTO!")
        print("No he Podido Adivinar :(")

        nueva_pregunta = input("Ingresa una Nueva Pregunta: ")
        objeto_usuario = input("Cual era tu Objeto?: ")
        print("Cual es la Respuesta Correcta para tu Objeto? (SI/NO)")

        respuesta_usuario = input()
        nuevo_nodo_pregunta = Nodo(nueva_pregunta)
        if respuesta_usuario.lower() == "sí":
            nuevo_nodo_pregunta.izquierda = Nodo(objeto_usuario)
            nuevo_nodo_pregunta.derecha = nodo_actual
        else:
            nuevo_nodo_pregunta.derecha = Nodo(objeto_usuario)
            nuevo_nodo_pregunta.izquierda = nodo_actual
        if nodo_actual == raiz:
            raiz = nuevo_nodo_pregunta

raiz = None

#MENU PRINCIPAL
while True:
    print("\n         JUEGO DE ADIVINANZAS")
    print("\n1. Construir Adivinanzas")
    print("2. Iniciar el Juego")
    print("3. Adivinar y Aprender")
    print("4. Reiniciar el Juego")
    print("5. Exportar Archivo")
    print("0. SALIR")

    opcion = input("\nIngrese el Número de la Opción que Desee: ")

    if opcion == "1":
        while True:
            print("\n           CONSTRUIR ADIVINANZAS")
            print("\n1. Ingresar las Preguntas Manualmente")
            print("2. Usar Preguntas Predeterminadas")
            print("3. REGRESAR AL MENU PRINCIPAL")

            opcion = input("\nIngrese el Número de la Opción que Desee: ")

            if opcion == "1":
                while True:
                    print("\n         INGRESAR LAS PREGUNTAS MANUALMENTE")
                    print("\n1. Insertar a la Izquierda")
                    print("2. Insertar a la Derecha")
                    print("3. REGRESAR AL MENU PRINCIPAL")

                    opcion = input("\nIngrese el Número de la Opción que Desee: ")

                    if opcion == "1":
                        print("\n           INSERTAR A LA IZQUIERDA")
                        valor = input("Ingrese la Pregunta que Desea: ")
                        raiz = Insertar_Izquierda(raiz, valor)

                    elif opcion == "2":
                        print("\n           INSERTAR A LA DERECHA")
                        valor = input("Ingrese la Pregunta que Desea: ")
                        raiz = Insertar_Derecha(raiz, valor)

                    elif opcion == "3":
                        break

                    else:
                        print("\n¡ERROR!")
                        print("Opción Invalida. Intente de Nuevo")

            elif opcion == "2":
                print("")

            elif opcion == "3":
                break

            else:
                print("\n¡ERROR!")
                print("Opción Invalida. Intente de Nuevo")

    elif opcion == "2":
        Iniciar_Juego(raiz)

    elif opcion == "3":
        print("ADIVINAR Y APRENDER")

    elif opcion == "4":
        print("REINICIAR EL JUEGO")

    elif opcion == "5":
        print("EXPORTAR ARCHIVOS")

    elif opcion == "0":
        print("GRACIAS POR UTILIZAR MI PROGRAMA :)")
        print("Programa Hecho Por: Angie Melissa Santiago Rodriguez - 1555123")
        break

    else:
        print("\n¡ERROR!")
        print("Opcion Invalida. Intente de Nuevo")

