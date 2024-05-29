from random import randint


class JuegoBarcos:
    Tamaño_Barco = 0
    turnos = 0

    def __init__(self, TamañoDeTablero, NumeroDeTurno, NombreDeUsuario):
        self.Set_Tamaño_Tablero(TamañoDeTablero)
        self.Set_Turnos(NumeroDeTurno)
        self.Setusuario(NombreDeUsuario)
        self.tablero = []
        for x in range(self.Tamaño_Barco):
            self.tablero.append(["·"] * self.Tamaño_Barco)
        self.filaBarco = self.filaAleatoria()
        self.columnaBarco = self.columnaAleatoria()

    def Set_Tamaño_Tablero(self, Numero_tamaño):
        if not isinstance(Numero_tamaño, int):
            raise Exception("El tamaño del tablero debe de ser un número entero")
        if Numero_tamaño < 3:
            raise Exception("El mínimo tamaño del tablero es 3")
        if Numero_tamaño > 9:
            raise Exception("El máximo tamaño del tablero es 9")
        self.Tamaño_Barco = Numero_tamaño

    def GetTamañoBarco(self):
        return self.Tamaño_Barco

    def Set_Turnos(self, NumeroDeTurnos):
        if not isinstance(NumeroDeTurnos, int):
            raise Exception("El Numero de turno debe de ser un número entero")
        if NumeroDeTurnos < 5:
            raise Exception("Al menos deben de haber 5 turnos")
        if NumeroDeTurnos > self.Tamaño_Barco * self.Tamaño_Barco:
            raise Exception("Demasiados turnos para el tamaño del tablero")
        self.turnos = NumeroDeTurnos

    def GetTurno(self):
        return self.turnos

    def Setusuario(self, NombreDeUsuario):
        self.NombreDeusuario = NombreDeUsuario

    def Getusuario(self):
        return self.NombreDeusuario

    def Mi_Tablero(self):

        Lista_Orizontal = "  | "
        for NumeroDeFila in range(self.Tamaño_Barco):
            Lista_Orizontal += str(NumeroDeFila) + " "
        print(Lista_Orizontal)

        lista_vertical = "--+-"
        for NumeroDeFila in range(self.Tamaño_Barco):
            lista_vertical += "--"
        print(lista_vertical)

        NumeroDeFila = 0
        for Fila in self.tablero:
            print(str(NumeroDeFila) + " | " + " ".join(Fila))
            NumeroDeFila += 1

    def filaAleatoria(self):
        return randint(0, self.Tamaño_Barco - 1)

    def columnaAleatoria(self):
        return randint(0, self.Tamaño_Barco - 1)

    def Juego(self):
        print("¡Juguemos a la guerra de barcos!")
        self.Mi_Tablero()
        for Turno in range(self.GetTurno()):
            print(f"Te quedan {self.GetTurno() - Turno} turnos")
            print("")
            print("Indica la posición que quieres bombardear:")
            Fila = int(input("Fila: "))
            Columna = int(input("Columna: "))

            if Fila == self.filaBarco and Columna == self.columnaBarco:
                print("¡Enhorabuena! Hundiste mi barco.")
                self.tablero[Fila][Columna] = "B"
                self.Mi_Tablero()
                break
                if self.tablero[Fila][Columna] == "B":
                    print("¡Bomb!")
            else:
                if (Fila < 0 or Fila >= self.GetTamañoBarco()) or (
                        Columna < 0 or Columna >= self.GetTamañoBarco()):
                    print("Has indicado una posición fuera del tablero.")
                elif self.tablero[Fila][Columna] == "X":
                    print("Esa posición ya la habías adivinado.")
                else:
                    print("¡Fallaste!")
                    self.tablero[Fila][Columna] = "X"

                self.Mi_Tablero()
                if Turno + 1 == self.GetTurno():
                    print(" GAME OVER ")
                    self.tablero[Fila][Columna] = "B"
                    self.Mi_Tablero()

                if self.GetTurno() == self.GetTurno() - 2:
                    print(" Queda poco para terminar ")
                    self.tablero[Fila][Columna] = "?"
                    self.Mi_Tablero()


try:
    TamañoDeTablero = int(input("Introduce el tamaño del tablero"))
    NumeroDeTurno = int(input("Introduce el cantidad de turno"))
    NombreDeUsuario = input("Introduce tu nombre")
    juego = JuegoBarcos(TamañoDeTablero, NumeroDeTurno, NombreDeUsuario)
    juego.Juego()
except Exception as e:
    print(f"Algo no ha ido bien: {e}")
