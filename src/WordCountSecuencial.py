

def puntuation(paraula):
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

if __name__ == "__main__":

    #f = open ("sherlock2.txt")
    f = open ("Quijote.txt")
    #f = open ("bible.txt")
    #f = open ("fitxeroProva.txt")
    contador = 0

    for line in f:
        for paraula in line.split():
            paraula = puntuation(paraula)
            
            if(paraula.find(" ")>=0):
                for p in paraula.split():
                    contador+=1

            else:
                contador+=1

    print contador
    f.close()
