from pyactor.context import set_context, create_host, Host, sleep, shutdown, serve_forever
from pyactor.exceptions import TimeoutError
import os
import os.path as path
import time

if __name__ == "__main__":

    set_context()
    host = create_host('http://127.0.0.1:1600')
    
    url = "http://127.0.0.1:8000/sherlock.txt"
    filename = url[url.rfind("/") +1 :]

    if(path.exists(filename) != True):
            os.system("curl -O "+url)

    contadorLinia = 0
    
    f = open(filename)
    contadorLinia = len(f.readlines())
    f.close()

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'RegistryM', 'Registry')    
    reducer = registry.lookup("Reduce")                  #agafem url reduce del registry
    
    registry.unbind("Reduce")                           #l'eliminem delr egistri per a que no molesti al for
    registryAll = registry.get_all()                    #agafem tots els altres
    totalMappers = len(registryAll)                     #mirem quants n'hi ha per dividir el fitxer

    aux = contadorLinia % totalMappers
    contadorLinia = contadorLinia + totalMappers - aux      #per que sigui multiple

    r = reducer.spawn('Reducer', 'ReduceMapper/Word')
    h = host.spawn('Master', 'Echo/Word')

    i = 0;

    print "Esperant Mappers per contar paraules..."

    t = time.time()

    for remote_host in registryAll:

        if remote_host is not None:
            print remote_host
            mapper = remote_host.spawn('mapperW', 'WordCount/Word')
            mapper.wordCount(url, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers, t)
        i = i+1;

    i=0

    raw_input()

    t = time.time()
 
    for remote_host in registryAll:

        if remote_host is not None:
            print remote_host
            mapper = remote_host.spawn('mapperC', 'CountWord/Word')
            mapper.countWord(url, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers, t)
        i = i+1;
  
  #wait until Reduce finishes

    serve_forever()
