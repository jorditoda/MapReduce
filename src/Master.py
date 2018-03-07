from pyactor.context import set_context, create_host, Host, sleep, shutdown
from pyactor.exceptions import TimeoutError

class Word(object):
    _ask = {'wordCount', 'puntuation', 'countWord'}                #asincron
    _tell = ['']                #sincron

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

    def wordCount(self, fitxer, inici, fi):
        f = open (fitxer)
        
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

        return contador

    def add(self, paraula, diccionari):
        if (paraula not in diccionari):
            diccionari[paraula] = 1
        else:
            aux = diccionari[paraula]
            diccionari[paraula] = aux+1

        return diccionari

    def countWord(self, fitxer, inici, fi):
        f = open (fitxer)
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

        return diccionari


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')
    fitxer = "sherlock.txt"
    contadorLinia = 0

    f = open (fitxer, 'r')
    contadorLinia = (len(f.readlines()))

    f.close()

    if (contadorLinia %2 ==1):
        contadorLinia+=1

    remote_host1 = host.lookup_url('http://127.0.0.1:1278/', Host)
    remote_host2 = host.lookup_url('http://127.0.0.1:1279/', Host)
    #print remote_host
    mapper1 = remote_host1.spawn('mapper1', 'Master/Word')
    mapper2 = remote_host2.spawn('mapper2', 'Master/Word')


    
    print mapper1.wordCount(fitxer, 0, contadorLinia/2)
    print mapper1.countWord(fitxer, 0, contadorLinia/2)
    print mapper2.wordCount(fitxer, contadorLinia/2, contadorLinia)
    print mapper2.countWord(fitxer, contadorLinia/2, contadorLinia)
    
    shutdown()