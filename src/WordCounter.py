class Word(object):
    _ask = {''}                #sincron
    _tell = ['wordCount', 'puntuation', 'countWord']                #asincron

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

    h = create_host()
    e1 = h.spawn('WordC', Word)