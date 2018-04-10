from pyactor.context import set_context, create_host, sleep, shutdown
import time
import os
import os.path as path

class Word(object):
    _tell = ['wordCount', 'countWord', 'reduceW', 'reduceC','echo']                #asincron
    _ref = ['wordCount', 'countWord', 'reduceW', 'reduceC']

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

    def echo(self, string):
        print string

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

    def puntuation(self, paraula):
        paraula = paraula.replace('*','')
        paraula = paraula.replace('.','')
        paraula = paraula.replace('-',' ')
        paraula = paraula.replace('_',' ')
        paraula = paraula.replace('?','')
        paraula = paraula.replace('!','')
        paraula = paraula.replace(',','')
        paraula = paraula.replace('(','')
        paraula = paraula.replace(')','')
        paraula = paraula.replace('[','')
        paraula = paraula.replace(']','')
        paraula = paraula.replace('\'','')
        paraula = paraula.replace('\"','')
        paraula = paraula.replace('=',' ')
        paraula = paraula.replace('#',' ')
        paraula = paraula.replace(':',' ')
        paraula = paraula.replace(';',' ')
        paraula = paraula.replace('/',' ')
        return paraula.lower()

    def wordCount(self, url, inici, fi, r, host, numMapper, now):

        filename = url[url.rfind("/") +1 :]

        if(path.exists(filename) != True):
            os.system("curl -O "+url)

        f = open(filename)

        print "fitxer obert"

        contador = 0
        contadorLinia = 0

        for line in f:
            if (contadorLinia >= inici and contadorLinia < fi):

                for paraula in line.split():
                    paraula = self.puntuation(paraula)

                    if(paraula.find(" ")>=0):
                        for p in paraula.split():
                            contador+=1

                    else:
                        contador+=1

            contadorLinia +=1
        f.close()
        r.reduceC(contador, host, numMapper, now)

    def add(self, paraula, diccionari):
        if (paraula not in diccionari):
            diccionari[paraula] = 1
        else:
            aux = diccionari[paraula]
            diccionari[paraula] = aux+1

        return diccionari

    def countWord(self, url, inici, fi, r, host, numMapper, now):

        filename = url[url.rfind("/") +1 :]

        if(path.exists(filename) != True):
            os.system("curl -O "+url)

        f = open(filename)

        diccionari = {}

        contadorLinia = 0

        for line in f:
            if (contadorLinia >= inici and contadorLinia < fi):

                for paraula in line.split():
                    paraula = self.puntuation(paraula)

                    if(paraula.find(" ")>=0):
                        for p in paraula.split():
                            diccionari = self.add(p, diccionari)

                    else:
                        diccionari = self.add(paraula, diccionari)

            contadorLinia +=1
        f.close()

        r.reduceW(diccionari, host, numMapper, now)


if __name__ == "__main__":
    set_context()
