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
            raise Exception("La grandària del tauler ha de ser un nombre enter")
        if Numero_tamaño < 3:
            raise Exception("La mínima grandària del tauler és 3")
        if Numero_tamaño > 9:
            raise Exception("La màxima grandària del tauler és 9")
        self.Tamaño_Barco = Numero_tamaño

    def GetTamañoBarco(self):
        return self.Tamaño_Barco

    def Set_Turnos(self, NumeroDeTurnos):
        if not isinstance(NumeroDeTurnos, int):
            raise Exception("El Numere de torn ha de ser un nombre enter")
        if NumeroDeTurnos < 5:
            raise Exception("Almenys han d'haver-hi 5 torns")
        if NumeroDeTurnos > self.Tamaño_Barco * self.Tamaño_Barco:
            raise Exception("Massa torns per a la grandària del tauler")
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
        print("¡Juguem a la guerra de vaixells!!")
        self.Mi_Tablero()
        for Turno in range(self.GetTurno()):
            print(f"Et queden {self.GetTurno() - Turno} torns")
            print("")
            print("Indica la posició que vols bombardejar:")
            Fila = int(input("Fila: "))
            Columna = int(input("Columna: "))

            if Fila == self.filaBarco and Columna == self.columnaBarco:
                print("Enhorabona! Vas afonar el meu vaixell.")
                self.tablero[Fila][Columna] = "B"
                self.Mi_Tablero()
                break
                if self.tablero[Fila][Columna] == "B":
                    print("¡Bomb!")
            else:
                if (Fila < 0 or Fila >= self.GetTamañoBarco()) or (
                        Columna < 0 or Columna >= self.GetTamañoBarco()):
                    print("Has indicat una posició fora del tauler.")
                elif self.tablero[Fila][Columna] == "X":
                    print("Eixa posició ja l'havies endevinada.")
                else:
                    print("Vas fallar!")
                    self.tablero[Fila][Columna] = "X"

                self.Mi_Tablero()
                if Turno + 1 == self.GetTurno():
                    print(" HAS PERDUT ")
                    self.tablero[Fila][Columna] = "B"
                    self.Mi_Tablero()

                if self.GetTurno() == self.GetTurno() - 2:
                    print(" Queda poco para terminar ")
                    self.tablero[Fila][Columna] = "?"
                    self.Mi_Tablero()


try:
    TamañoDeTablero = int(input("Queda poc per a acabar"))
    NumeroDeTurno = int(input("Introduïx el quantitat de torn"))
    NombreDeUsuario = input("Introduïx el teu nom")
    juego = JuegoBarcos(TamañoDeTablero, NumeroDeTurno, NombreDeUsuario)
    juego.Juego()
except Exception as e:
    print(f"Alguna cosa no ha anat bé: {e}")
