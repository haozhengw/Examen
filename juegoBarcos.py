from random import randint


class JuegoBarcos:
    __tamanyo = 0
    __turnos = 0

    def __init__(self, ntamanyo, nturnos):
        self.setTa(ntamanyo)
        self.setTu(nturnos)
        self.tablero = []
        for x in range(self.__tamanyo):
            self.tablero.append(["·"] * self.__tamanyo)
        self.filaBarco = self.filaAleatoria()
        self.columnaBarco = self.columnaAleatoria()

    def setTa(self, ntamanyo):
        if not isinstance(ntamanyo, int):
            raise Exception("El tamaño del tablero debe de ser un número entero")
        if ntamanyo < 3:
            raise Exception("El mínimo tamaño del tablero es 3")
        if ntamanyo > 9:
            raise Exception("El máximo tamaño del tablero es 9")
        self.__tamanyo = ntamanyo

    def getTa(self):
        return self.__tamanyo

    def setTu(self, nturnos):
        if not isinstance(nturnos, int):
            raise Exception("El tamaño del tablero debe de ser un número entero")
        if nturnos < 5:
            raise Exception("Al menos deben de haber 5 turnos")
        if nturnos > self.__tamanyo * self.__tamanyo:
            raise Exception("Demasiados turnos para el tamaño del tablero")
        self.__turnos = nturnos

    def getTu(self):
        return self.__turnos

    def mT(self):

        li1 = "  | "
        for i in range(self.__tamanyo):
            li1 += str(i) + " "
        print(li1)

        li2 = "--+-"
        for i in range(self.__tamanyo):
            li2 += "--"
        print(li2)

        i = 0
        for f in self.tablero:
            print(str(i) + " | " + " ".join(f))
            i += 1

    def filaAleatoria(self):
        return randint(0, self.__tamanyo - 1)

    def columnaAleatoria(self):
        return randint(0, self.__tamanyo - 1)

    def j(self):
        print("¡Juguemos a la guerra de barcos!")
        self.mT()
        for t in range(self.getTu()):
            print(f"Te quedan {self.getTu() - t} turnos")
            print("")
            print("Indica la posición que quieres bombardear:")
            f = int(input("Fila: "))
            c = int(input("Columna: "))

            if f == self.filaBarco and c == self.columnaBarco:
                print("¡Enhorabuena! Hundiste mi barco.")
                self.tablero[f][c] = "B"
                self.mT()
                break
                if self.tablero[f][c] == "B":
                    print("¡Bomb!")
            else:
                if (f < 0 or f >= self.getTa()) or (
                        c < 0 or c >= self.getTa()):
                    print("Has indicado una posición fuera del tablero.")
                elif self.tablero[f][c] == "X":
                    print("Esa posición ya la habías adivinado.")
                else:
                    print("¡Fallaste!")
                    self.tablero[f][c] = "X"

                self.mT()
                if t + 1 == self.getTu():
                    print(" GAME OVER ")
                    self.tablero[f][c] = "B"
                    self.mT()

                if self.getTu() == self.getTu() - 2:
                    print(" Queda poco para terminar ")
                    self.tablero[f][c] = "?"
                    self.mT()


try:
    juego = JuegoBarcos(8, 10)
    juego.j()
except Exception as e:
    print(f"Algo no ha ido bien: {e}")
