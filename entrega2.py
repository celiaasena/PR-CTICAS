TAMANYO_TABLERO: int = 8                           #estan en letras mayusculas porque son constantes, es decir, no van a cambiar
LETRAS_VALIDAS: str = "abcdefgh"
NUMEROS_VALIDOS: str = "12345678"

class Pieza:   #pieza de ajedrez generica
    """pieza de ajedrez generica"""

    def __init__(self, color: str, simbolo: str, nombre: str) -> None: 
        """crea una pieza con su color, simbolo, y nombre"""

        self.color: str = color 
        self.simbolo: str = simbolo 
        self.nombre: str = nombre 

  
    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], destino: tuple[int, int]) -> bool:    
        """True si la pieza puede ir de origen a destino segun sus reglas"""

        return False      # cada subclase lo redefinira
  
  
class Torre(Pieza):  #torre hereda a Pieza
    """Torre: se mueve en linea recta por filas o columnas"""
    
    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], destino: tuple[int, int]) -> bool: 
        """True si el movimiento es en linea recta y el camino esta libre"""

        if origen[0] != destino[0] and origen[1] != destino[1]:      #si en el movimiento cambia la fila y de columna, el movimiento no es valido porque una torre no se mueve asi para una torre
            return False          # ni misma fila ni misma columna 
        return tablero.camino_libre(origen, destino) 


class Caballo(Pieza):  
    """Caballo: se mueve en forma de L"""
    
    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], destino: tuple[int, int]) -> bool: 
        """True si el movimiento es en L y el camino esta libre"""



class Alfil(Pieza): 
    """Torre: se mueve en diagonal"""
    
    def es_movimiento_valido(self, tablero: "Tablero", origen: tuple[int, int], destino: tuple[int, int]) -> bool: 
        """True si el movimiento es en diagonal y el camino esta libre"""

        if abs(origen[0] - destino[0]) == abs(origen[1] - destino[1]):  #si la distancia entre la fila de origen ([0]) y la de destino es igual y lo mismo con la columna ([1]), entonces se esta moviendo en diagonal
            return True          # no es diagonal
        return tablero.camino_libre(origen, destino)


class Reina(Pieza):
    """Reina: se mueve en linea recta o diagonal pero no en L """
class Rey(Pieza):
    """Rey: se mueve en todas direcciones pero solo de 1 en 1 """
class Peon(Pieza):
    """Peon: solo se mueve hacia delante de 1 en 1, o avanza 2 en el primer movimiento"""

class Tablero:   #guarda la posicion de las piezas y las operaciones sobre el tablero
  
    def __init__(self) -> None: 
        self.casillas: list[list[Pieza | None]] = []   # 8 filas de 8 casillas 
        for fila in range(8):
            fila_vacia: list[Pieza | None] = [None] * 8
            self.casillas.append(fila_vacia)
        self.colocar_posicion_inicial() 
            
    def colocar_posicion_inicial(self) -> None:   #Rellena el tablero con la posicion inicial estandar.""" 
        for columna in range(8):
            self.casillas[1][columna] = Peon("blanca", "\u2659", "peon")
        self.casillas[0][0] = Torre("blanca", "\u2656", "torre")
        self.casillas[0][1] = Caballo("blanca", "\u2658", "caballo")
        self.casillas[0][2] = Alfil("blanca", "\u2657", "alfil")
        self.casillas[0][3] = Reina("blanca", "\u2655", "reina")
        self.casillas[0][4] = Rey("blanca", "\u2654", "rey")
        self.casillas[0][5] = Alfil("blanca", "\u2657", "alfil")
        self.casillas[0][6] = Caballo("blanca", "\u2658", "caballo")
        self.casillas[0][7] = Torre("blanca", "\u2656", "torre")
            
        for columna in range(8):
            self.casillas[6][columna] = Peon("negra", "\u265F", "peon")
        self.casillas[7][0] = Torre("negra", "\u265C", "torre")
        self.casillas[7][1] = Caballo("negra", "\u265E", "caballo")
        self.casillas[7][2] = Alfil("negra", "\u265D", "alfil")
        self.casillas[7][3] = Reina("negra", "\u265B", "reina")
        self.casillas[7][4] = Rey("negra", "\u265A", "rey")
        self.casillas[7][5] = Alfil("negra", "\u265D", "alfil")
        self.casillas[7][6] = Caballo("negra", "\u265E", "caballo")
        self.casillas[7][7] = Torre("negra", "\u265C", "torre")



    def imprimir_tablero(self) -> None:                       
       
        print("  a  b  c  d  e  f  g  h")

        for fila in range(7, -1, -1):                              
            linea: str = str(fila + 1)    
            for columna in range(8):
                pieza: Pieza | None = self.casillas[fila][columna]    
                if pieza is None:                                                  
                    linea: str = linea + "   "                                           
                else:                                                             
                    linea: str = linea + " " + pieza.simbolo + " "

            print(linea)



    def mover_pieza(self, origen: tuple[int, int], destino: tuple[int, int]) -> None:
        """mueve la pieza de origen a destino"""

        pieza: Pieza | None = self.casillas[origen[0]][origen[1]]    #guarda en pieza la casilla de origen, que puede ser una pieza o vacio (None)
        self.casillas[destino[0]][destino[1]] = pieza      #pone la pieza en el destino, si hay una pieza en el destino se sustituye
        self.casillas[origen[0]][origen[1]] = None       #deja la casilla de origen vacia                 



def es_casilla_valida(casilla: str) -> bool:      
    """devuelve True / False si la casilla es valida o no"""
    return len(casilla) == 2 and casilla[0] in LETRAS_VALIDAS and casilla[1] in NUMEROS_VALIDOS

def convertir_casilla(casilla: str) -> tuple[int, int]:
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
 
    fila_tablero: int = int(casilla[1]) - 1
    return (fila_tablero, columna)


def corregir_movimiento(casilla_para_limpiar: str) -> list[str]:
    """limpia el texto mal formulado. Si el formato no es valido devuelve una lista vacia"""
    
    limpio: str = casilla_para_limpiar.strip().lower()
    partes: list[str] = limpio.split()

    if len(partes) != 2:
        return []

    origen_valido: bool = es_casilla_valida(partes[0])
    destino_valido: bool = es_casilla_valida(partes[1])

    if origen_valido == False or destino_valido == False:
        return []

    return partes



def obtener_nombre_pieza(nombre_casilla: list[list[str]], casilla: str) -> str:   #devuelve el nombre de la pieza que hay en la casilla pedida
    fila_tablero, columna = convertir_casilla(casilla)
    return nombre_casilla[fila_tablero][columna]


# tablero: Tablero = Tablero()
# tablero.mover_pieza(convertir_casilla("e2"), convertir_casilla("e4"))
# tablero.imprimir_tablero()


def jugar() -> None:
    """Bucle principal de la partida"""

    tablero: Tablero = Tablero()
    estado: str = "turno_blancas"
    tablero.imprimir_tablero()

    while estado != "fin_partida":
        if estado == "turno_blancas":
            print("Turno de las blancas")
            casilla: str = input("Introduce una casilla (ej. e2 e4) o 'salir' para terminar: ")
            if casilla == "salir":
                estado = "fin_partida"
            else:
                partes: list[str] = corregir_movimiento(casilla)
                if partes == []:
                    print("Formato no válido. Escribe un formato valido, por ejemplo: e2 e4")
                else:
                    origen: tuple[int, int] = convertir_casilla(partes[0])
                    destino: tuple[int, int] = convertir_casilla(partes[1])
                    tablero.mover_pieza(origen, destino)
                    tablero.imprimir_tablero()
                    estado = "turno_negras"

        elif estado == "turno_negras":
            print("Turno de las negras")
            texto: str = input("Movimiento (ej. e2 e4) o 'salir': ")
            if texto == "salir":
                estado = "fin_partida"
            else:
                partes: list[str] = corregir_movimiento(texto)
                if partes == []:
                    print("Formato no válido. Escribe origen y destino, por ejemplo: e2 e4")
                else:
                    origen: tuple[int, int] = convertir_casilla(partes[0])
                    destino: tuple[int, int] = convertir_casilla(partes[1])
                    tablero.mover_pieza(origen, destino)
                    tablero.imprimir_tablero()
                    estado = "turno_blancas"

    print("Fin de la partida. ¡Hasta la próxima!")


jugar()