
from pyactor.context import set_context, create_host, sleep, shutdown
import time
import os
import os.path as path

class Word(object):
    _tell = [ 'reduceC', 'reduceW']                #asincron
    _ref = [ 'reduceC', 'reduceW']

    contadorMappers = 0
    contadorMappersW = 0
    w = 0
    dicc = {}

    def addR(self, paraula, diccionari, value):
        if (paraula not in diccionari):
            diccionari[paraula] = value
        else:
            aux = diccionari[paraula]
            diccionari[paraula] = aux+value

        return diccionari

    def reduceW(self, d, m, numMap, now):

        self.contadorMappersW+=1
        for key, value in d.items():
            self.addR(key, self.dicc, value)

        if(self.contadorMappersW == numMap):
            elapsed = (time.time() - now)
            m.echo(self.dicc)
            m.echo("Temps emprat amb diccionari:")
            m.echo(elapsed)

    def reduceC(self, words, m, numMap, now):

        self.contadorMappers+=1
        self.w = self.w + words

        if(self.contadorMappers == numMap):
            elapsed = (time.time() - now)
            m.echo("Numero paraules: ")
            m.echo(self.w)
            m.echo("Temps emprat contant:")
            m.echo(elapsed)
            m.echo("\nPrem qualsevol tecla per continuar i crear el diccionari\n")


if __name__ == "__main__":
    set_context()
