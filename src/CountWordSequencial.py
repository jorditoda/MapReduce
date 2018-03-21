
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

def add(paraula):
    if (paraula not in diccionari):
        diccionari[paraula] = 1
    else:
        aux = diccionari[paraula]
        diccionari[paraula] = aux+1

if __name__ == "__main__":

    #f = open ("sherlock2.txt")
    #f = open ("Quijote.txt")
    f = open ("bible2.txt")
    #f = open ("fitxeroProva.txt")
    diccionari = {}

    for line in f.readlines():
        for paraula in line.split():
            
            paraula = puntuation(paraula)
            
            if(paraula.find(" ")>=0):
                for p in paraula.split():
                    add(p)

            else:
                add(paraula)

    print diccionari
    f.close()

