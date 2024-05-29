from random import randint


class JuegoBarcos:

    turnos = 0


    def __init__(self, TamañoDeTablero, NumeroDeTurno, NombreDeUsuario):
        self.Set_Tamaño_Tablero(TamañoDeTablero)
        self.Set_Turnos(NumeroDeTurno)
        self.Setusuario(NombreDeUsuario)
        self.tablero = []
        for x in range(self.Tamaño_Tablero):
            self.tablero.append(["·"] * self.Tamaño_Tablero)
        self.filaBarco = self.filaAleatoria()
        self.columnaBarco = self.columnaAleatoria()
        self.filaBarco2 = self.filaAleatoria()
        self.columnaBarco2 = self.columnaAleatoria()
        self.filaBarco3 = self.filaAleatoria()
        self.columnaBarco3 = self.columnaAleatoria()

    def Set_Tamaño_Tablero(self, Numero_tamaño):
        if not isinstance(Numero_tamaño, int):
            raise Exception("El tamaño del tablero debe de ser un número entero")
        if Numero_tamaño < 3:
            raise Exception("El mínimo tamaño del tablero es 3")
        if Numero_tamaño > 9:
            raise Exception("El máximo tamaño del tablero es 9")
        self.Tamaño_Tablero = Numero_tamaño

    def GetTamañoTablero(self):
        return self.Tamaño_Tablero

    def Set_Turnos(self, NumeroDeTurnos):
        if not isinstance(NumeroDeTurnos, int):
            raise Exception("El Numero de turno debe de ser un número entero")
        if NumeroDeTurnos < 5:
            raise Exception("Al menos deben de haber 5 turnos")
        if NumeroDeTurnos > self.Tamaño_Tablero * self.Tamaño_Tablero:
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
        for NumeroDeFila in range(self.Tamaño_Tablero):
            Lista_Orizontal += str(NumeroDeFila) + " "
        print(Lista_Orizontal)

        lista_vertical = "--+-"
        for NumeroDeFila in range(self.Tamaño_Tablero):
            lista_vertical += "--"
        print(lista_vertical)

        NumeroDeFila = 0
        for Fila in self.tablero:
            print(str(NumeroDeFila) + " | " + " ".join(Fila))
            NumeroDeFila += 1

    def filaAleatoria(self):
        return randint(0, self.Tamaño_Tablero - 1)

    def columnaAleatoria(self):
        return randint(0, self.Tamaño_Tablero - 1)

    def Juego(self,):
        NumeroBarcoUndidio = 0;
        print("¡Juguemos a la guerra de barcos!")
        self.Mi_Tablero()

        for Turno in range(self.GetTurno()):
            BarcoUndido = False
            print(f"Te quedan {self.GetTurno() - Turno} turnos")
            print("")
            print("Indica la posición que quieres bombardear:")
            Fila = int(input("Fila: "))
            Columna = int(input("Columna: "))

            print(f"{self.filaBarco} + {self.columnaBarco}")
            print(f"{self.filaBarco2} + {self.columnaBarco2}")
            print(f"{self.filaBarco3} + {self.columnaBarco3}")
            print(NumeroBarcoUndidio)



            if Fila == self.filaBarco and Columna == self.columnaBarco:
                self.tablero[Fila][Columna] = "B"
                self.Mi_Tablero()
                NumeroBarcoUndidio = NumeroBarcoUndidio + 1
                BarcoUndido = True
                if self.tablero[Fila][Columna] == "B":
                    print("¡Bomb!")
                    if NumeroBarcoUndidio == 3:
                        print("Has Ganado!")
                        break
            elif Fila == self.filaBarco2 and Columna == self.columnaBarco2:
                self.tablero[Fila][Columna] = "B"
                self.Mi_Tablero()
                BarcoUndido = True
                NumeroBarcoUndidio = NumeroBarcoUndidio + 1
                if self.tablero[Fila][Columna] == "B":
                    print("¡Bomb!")
                    if NumeroBarcoUndidio == 3:
                        print("Has Ganado!")
                        break
            elif Fila == self.filaBarco3 and Columna == self.columnaBarco3:
                self.tablero[Fila][Columna] = "B"
                self.Mi_Tablero()
                BarcoUndido = True
                NumeroBarcoUndidio = NumeroBarcoUndidio + 1
                if self.tablero[Fila][Columna] == "B":
                    print("¡Bomb!")
                    if NumeroBarcoUndidio == 3:
                        print("Has Ganado!")
                        break


            elif BarcoUndido == False:

                if (Fila < 0 or Fila >= self.GetTamañoTablero()) or (
                        Columna < 0 or Columna >= self.GetTamañoTablero()):
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
