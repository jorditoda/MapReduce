from pyactor.context import set_context, create_host, Host, sleep, shutdown
from pyactor.exceptions import TimeoutError

class Word(object):
    _ask = {'wordCount', 'puntuation', 'countWord'}                #sincron
    #_tell = ['wordCount', 'puntuation', 'countWord']                #asincron

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
        print "he entrat :D"

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
        print contador

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
        print "he sortir del countword"
        return diccionari



if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1679')
    fitxer = "sherlock.txt"
    contadorLinia = 0

    f = open (fitxer, 'r')
    contadorLinia = (len(f.readlines()))

    f.close()

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry',
                               's4_registry')
    registryAll = registry.get_all()
    totalMappers = len(registryAll)

    aux = contadorLinia % totalMappers
    contadorLinia = contadorLinia + totalMappers - aux

    for remote_host in registryAll:

        if remote_host is not None:
            if not remote_host.has_actor('server'):
                print "mapper :D"
"""
                server = remote_host.spawn('server', 's4_clientb/Server')
            else:
                server = remote_host.lookup('server')
            z = server.add(6, 7)
          
        try:
            registry.unbind('None')
        except NotFound:
            print "Cannot unbind this object: is not in the registry."  
"""


"""    remote_host1 = host.lookup_url('http://127.0.0.1:1278/', Host)
    remote_host2 = host.lookup_url('http://127.0.0.1:1279/', Host)
    remote_host3 = host.lookup_url('http://127.0.0.1:1280/', Host)
    print remote_host1
    mapper1 = remote_host1.spawn('mapper1', 'Master/Word')
    print mapper1
    mapper2 = remote_host2.spawn('mapper2', 'Master/Word')
    mapper3 = remote_host3.spawn('mapper3', 'Master/Word')"""

"""
    print mapper1.wordCount(fitxer, 0, contadorLinia/totalMappers)
    print mapper1.countWord(fitxer, 0, contadorLinia/totalMappers)
    print mapper2.wordCount(fitxer, contadorLinia/totalMappers, (contadorLinia/totalMappers)*2)
    print mapper2.countWord(fitxer, contadorLinia/totalMappers, (contadorLinia/totalMappers)*2)
    print mapper3.wordCount(fitxer, (contadorLinia/totalMappers)*2, contadorLinia)
    print mapper3.countWord(fitxer, (contadorLinia/totalMappers)*2, contadorLinia)
   
"""
    #sleep(5)
    print "he acabat"
    print "GOOD NIGHT"
    shutdown()