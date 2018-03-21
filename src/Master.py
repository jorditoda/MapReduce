from pyactor.context import set_context, create_host, Host, sleep, shutdown, serve_forever
from pyactor.exceptions import TimeoutError
from urllib import urlopen

if __name__ == "__main__":
    #now = time.time()
    set_context()
    host = create_host('http://127.0.0.1:1600')
    
    url = "http://127.0.0.1:8000/bible.txt"
    fitxer = urlopen(url)
    filename = url[url.rfind("/") +1 :]

    f = open(filename)

    contadorLinia = 0
    
    contadorLinia = len(f.readlines())
    f.close()


    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'RegistryM', 'Registry')
    reducer = registry.lookup("Reduce")                  #agafem url reduce del registry
    registry.unbind("Reduce")                           #l'eliminem delr egistri per a que no molesti al for
    registryAll = registry.get_all()                    #agafem tots els altres

    totalMappers = len(registryAll)                     #mirem quants n'hi ha per dividir el fitxer

    aux = contadorLinia % totalMappers
    contadorLinia = contadorLinia + totalMappers - aux

    r = reducer.spawn('Reducer', 'WordCounter/Word')
    h = host.spawn('Master', 'WordCounter/Word')

    i = 0;

    print "Esperant Mappers..."

    for remote_host in registryAll:

        if remote_host is not None:
            print remote_host
            mapper = remote_host.spawn('mapper', 'WordCounter/Word')
            mapper.wordCount(url, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers)
            mapper.countWord(url, (contadorLinia/totalMappers)*i, (contadorLinia/totalMappers)*(i+1), r, h, totalMappers)
        i = i+1;
  
  #wait until Reduce finishes

    serve_forever()