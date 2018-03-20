from pyactor.context import set_context, create_host, Host, sleep, shutdown, serve_forever
from pyactor.exceptions import TimeoutError

class Word(object):
    #_ask = {'wordCount', 'countWord'}                #sincron
    _tell = ['wordCount', 'countWord', 'reduceW', 'reduceC','echi']                #asincron
    _ref = ['wordCount', 'countWord', 'reduceW', 'reduceC'] 

    contadorMappers = 0
    contadorMappersW = 0
    w = 0
    dicc = {}

    def echi(self, string):
        print string

    def reduceW(self, d, m, numMap):

        self.contadorMappersW+=1
        print "jo el d "
        print d
        #self.dicc.append(d)
        #self.dicc.update(d)
        print " jo soc el dicc  :DD"
        #self.dicc = {key: math.fsum(value) for key, value in d.items()}
        #for key, value in d.items():
            #self.dicc[key] = sum(value)

        print self.dicc

        if(self.contadorMappersW == numMap):          #aquest numero l'han de passar
            m.echi(self.dicc)

    def reduceC(self, words, m, numMap):

        self.contadorMappers+=1
        self.w = self.w + words

        if(self.contadorMappers == numMap):          #aquest numero l'han de passar
            m.echi(self.w) 

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

    def wordCount(self, fitxer, inici, fi, r, host, numMapper):
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
        
        r.reduceC(contador, host, numMapper)

    def add(self, paraula, diccionari):
        if (paraula not in diccionari):
            diccionari[paraula] = 1
        else:
            aux = diccionari[paraula]
            diccionari[paraula] = aux+1

        return diccionari

    def countWord(self, fitxer, inici, fi, r, host, numMapper):
        f = open (fitxer)
        diccionari = {}
        ''
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
        r.reduceW(diccionari, host, numMapper)



if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')
    fitxer = "sherlock.txt"
    contadorLinia = 0

    f = open (fitxer, 'r')
    contadorLinia = (len(f.readlines()))

    f.close()

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'RegistryM', 'Registry')
    reducer = registry.lookup("Reduce")                  #agafem url reduce del registry
    registry.unbind("Reduce")                           #l'eliminem delr egistri per a que no molesti al for
    registryAll = registry.get_all()                    #agafem tots els altres

    totalMappers = len(registryAll)                     #mirem quants n'hi ha per dividir el fitxer

    aux = contadorLinia % totalMappers
    contadorLinia = contadorLinia + totalMappers - aux

    r = reducer.spawn('Reducer', 'Master/Word')
    h = host.spawn('Master', 'Master/Word')

    i = 0;

    for remote_host in registryAll:

        if remote_host is not None:
            print remote_host
            mapper = remote_host.spawn('mapper', 'Master/Word')
            mapper.wordCount(fitxer, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers)
            mapper.countWord(fitxer, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers)
        i = i+1;

    #sleep(5)
    print "GOOD NIGHT"
    serve_forever()
    #shutdown()