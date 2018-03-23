from pyactor.context import set_context, create_host, serve_forever

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:1282/')
    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'RegistryM', 'Registry')

    registry.bind('Mapper5', host)

    
    serve_forever()



