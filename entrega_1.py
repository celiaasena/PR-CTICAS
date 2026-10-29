TAMANYO_TABLERO: int = 8                           #están en letras mayúsculas porque son constantes, es decir, no van a cambiar
LETRAS_VALIDAS: str = "abcdefgh"
NUMEROS_VALIDOS: str = "12345678"

tablero_simbolos: list[list[str]] = [                                                     #con una lista de listas creo una matriz (el tablero de ajedrez), donde cada fila es una lista
    ["\u265C", "\u265E", "\u265D", "\u265B", "\u265A", "\u265D", "\u265E", "\u265C"],     # en la fila 8 pongo las 8 piezas negras
    ["\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F", "\u265F"],     # en la fila 7 pongo los 8 peones negros
    ["", "", "", "", "", "", "", ""],                                                     # la fila 6 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 5 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 4 está vacía
    ["", "", "", "", "", "", "", ""],                                                     # la fila 3 está vacía
    ["\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659", "\u2659"],     # en la fila 2 pongo los 8 peones blancos
    ["\u2656", "\u2658", "\u2657", "\u2655", "\u2654", "\u2657", "\u2658", "\u2656"],     # en la fila 1 pongo las 8 piezas blancas
] 

tablero_nombres: list[list[str]] = [                    #con una lista de listas creo una matriz que le pone nombre a cada uno de las piezas de la matriz anterior
    ["Torre negra", "Caballo negro", "Alfil negro", "Reina negra", "Rey negro", "Alfil negro", "Caballo negro", "Torre negra"],
    ["Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro", "Peon negro"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""], 
    ["", "", "", "", "", "", "", ""],
    ["Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco", "Peon blanco"],
    ["Torre blanca", "Caballo blanco", "Alfil blanco", "Reina blanco", "Rey blanco", "Alfil blanco", "Caballo blanco", "Torre blanca"]
]

encabezado: str = "  "                                               #pongo una nueva variable vacia que va a ser el encabezado 
for indice_columna in range(TAMANYO_TABLERO):                        #creo un bucle con una nueva variable que es indice_columna, con tamaño TAMANYO_TABLERO, es decir, 8
    letra_columna: str = LETRAS_VALIDAS[indice_columna]              #pongo otra nueva variable que serán las letras que hay en cada columna, que recorrerá la letra que le corresponde (LETRAS_VALIDAS) respecto al indice
    encabezado: str = encabezado + " " + letra_columna + " "         #cuando ya ha seleccionado la letra y donde va a estar, imprime "encabezado" (que es un hueco), imprime otro hueco, la letra que corresponde y otro hueco. A partir de la segunda vuelta "encabezado" ya no lo imprime porque ya está reedefinido
print(encabezado)

#básicamente crea un bucle que recorra 8 veces (TAMANYO_TABLERO), donde en cada vuelta le corresponde una letra, y finalmente modifica la estética del bucle para que las letras estén separadas

for indice_fila in range(TAMANYO_TABLERO):                                 #creo un bucle con una nueva variable que es numero_fila, con tamaño TAMANYO_TABLERO, es decir, 8
    numero_fila: int = TAMANYO_TABLERO - indice_fila                       #como el tablero de ajedrez empieza en el 8 y de ahí va para abajo, el numero de fila será el tamaño del tablero (8) menos el numero de vueltas que haya dado el bucle, es decir, el indice.  EJ: quiero la fila 6: 8 (total) - 2 (lleva dos vueltas al bucle)
    linea: str = str(numero_fila) + " "                                    #creo una nueva variable, que es igual a numero_fila más un espacio. Además lo convierto en str porque econ int no puedo añadir el espacio
    for indice_columna in range(TAMANYO_TABLERO):                          #creo un bucle con una nueva variable que es indice_columna, con tamaño TAMANYO_TABLERO, es decir, 8
        simbolo: str = tablero_simbolos[indice_fila][indice_columna]       #defino una nueva variable que es el simbolo que hay en la casilla que le corresponde con respecto a su fila y columna (de la matriz tablero_simbolos)
        if simbolo == "":                                                  #si no hay pieza en la casilla solicitada
            celda: str = " . "                                             #entonces guarda un punto en la variable celda
        else:                                                              #en el caso contrario (sí hay pieza)
            celda: str = " " + simbolo + " "                               #entonces imprime un espacio, el simbolo y otro espacio (los espacios son para que quede más alineado)
        linea: str = linea + celda                                         #actualizo la variable linea, que es la que va construyendo el tablero, es decir, le voy añadiendo cada celda que va recorriendo el bucle
    print(linea)

print("")                                                                  #da un salto de línea para que no se vea el tablero y la frase pegadas
print("escribe una casilla (por ejemplo: e2) o 'salir' para terminar:")    #imprime la peticion de casilla o salida
print("")                                                                  #da un salto de línea

estado: str = "turno blancas"              #defino una variable que es el estado del juego, que empieza con turno de las blancas

while estado != "salir":                                                                               #mientras estado sea distinto a salir
    if estado == "turno blancas":  
        print("Turno de las blancas")                                                                  #si el estado esturno blancas, imprime 'turno de las blancas'
        casilla: str = input("Casilla a consultar, o 'salir' para terminar")                           #defino una variable que es casilla, donde pide al usuario una casilla o salir
        if casilla == "salir":  
            estado = "salir"                                                                           #si el usuario pone 'salir', el esatdo es salir y termina el bucle y se va al ultimo print (linea 131-132)
        elif len(casilla) == 2 and casilla[0] in LETRAS_VALIDAS and casilla[1] in NUMEROS_VALIDOS:     #si la longitud de la casilla es 2 (tiene 2 caracteres), la primera letra es valida, y el segundo caracter es un numero valido
            letra_columna: str = casilla [0]                                                           #vuelvo a definir letra_columna como el caracter 0 (el primero) de la casilla, que es la letra (EJ: e2, letra_columna = e)
            columna: int = 0                                                                           #defino la variable columna como 0, para que luego vaya aumentando según la letra que sea
            if letra_columna == "a":                                                                   #a partir de aquí creo un bucle para hacer que a cada letra que se introduzca le corresponda una columna. si la letra es a, entonces la columna es 0 (y así sucesivamente)
                columna: int = 0
            elif letra_columna == "b":
                columna: int = 1
            elif letra_columna == "c":
                columna = 2
            elif letra_columna == "d":
                columna = 3
            elif letra_columna == "e":
                columna = 4
            elif letra_columna == "f":
                columna = 5
            elif letra_columna == "g": 
                columna = 6
            elif letra_columna == "h":
                columna = 7

            fila_tablero: int = TAMANYO_TABLERO - int(casilla[1])              #creo una variable llamada fila_tablero, que es el tamaño del tablero (8) menos el numero de la casilla (EJ: e2, fila_tablero = 8 - 2 = 6, fila 6). esto es porque yo quiero e2, que será el peon blanco, pero en la matriz tablero_simbolos, el peon blanco está en la fila 6, porque el sistema python empieza a contar desde arriba, por lo que realmente contando desde arriba es la fila 6
            nombre_pieza: str = tablero_nombres[fila_tablero][columna]         #creo una nueva variable que son los nombres de cada pieza, que es el tablero_nombres en la fila y columna correspondientes

            if nombre_pieza != "":                                             #si el nombre de la pieza no está vacio (hay una pieza)
                print(f"en la casilla {casilla} hay: {nombre_pieza}")          #imprime esta frase con la casilla seleccionada y el nombre de la pieza que hay
            else:
                print(f"la casilla {casilla} esta vacia.")                     #si la casilla está vacia, imprime la frase

            estado = "turno negras"                                            #cambia el estado a turno de las negras para que en la siguiente vuelta del bucle sea el turno de las negras

        else:
            print("casilla no valida")                  #si el formato no es correcto el estado no cambia, sigue el turno negras hasta que se introduzca algo valido

    elif estado == "turno negras":                            #cuando el estado sea turno negras (lo acabamos de cambiar arriba)
        print("turno de las negras")                          #imprime 'turno de las negras'
        casilla: str = input("casilla: ")                     #y pide al usuario una casilla
                                                                                                       
       #AHORA ES EL MISMO PROCESO/BUCLE QUE EL TURNO DE LAS BLANCAS solo que el estado cambia a turno blancas, para que en la siguiente vuelta del bucle sea el turno de las blancas 
       
        if casilla == "salir":                                                                         
            estado = "salir"                                                                            
        elif len(casilla) == 2 and casilla [0] in LETRAS_VALIDAS and casilla[1] in NUMEROS_VALIDOS:     
            letra_columna: str = casilla [0]                                                            
            columna: int = 0                                                                           
            if letra_columna == "a":                                                                    
                columna: int = 0
            elif letra_columna == "b":
                columna: int = 1
            elif letra_columna == "c":
                columna = 2
            elif letra_columna == "d":
                columna = 3
            elif letra_columna == "e":
                columna = 4
            elif letra_columna == "f":
                columna = 5
            elif letra_columna == "g": 
                columna = 6
            elif letra_columna == "h":
                columna = 7

            fila_tablero: int = TAMANYO_TABLERO - int(casilla[1])
            nombre_pieza: str = tablero_nombres[fila_tablero][columna]

            if nombre_pieza != "":
                print(f"en la casilla {casilla} hay: {nombre_pieza}")
            else:
                print(f"la casilla {casilla} esta vacia")

            estado = "turno blancas"
        else:
            print("casilla no valida") 

print("")                                                #imprime una línea vacía
print("Fin de la partida. Hasta la próxima!")            #si estado es salir, se acaba el bucle e imprime esta frase 