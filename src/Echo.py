
from pyactor.context import set_context, create_host, sleep, shutdown
import time
import os
import os.path as path

class Word(object):
    _tell = [ 'echo']   


    def echo(self, string):
        print string

if __name__ == "__main__":
    set_context()
