
from pyactor.context import set_context, create_host, sleep, shutdown
import time
import os
import os.path as path

class Word(object):
    _tell = ['wordCount']                #asincron
    _ref = ['wordCount']

    contadorMappers = 0

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

if __name__ == "__main__":
    set_context()
