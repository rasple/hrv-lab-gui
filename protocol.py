from os.path import isfile
from os import remove
from threading import Thread, Lock

class Protocol:

    PROTOCOL_LOCATION='protocol.txt'
    mutex = Lock()

    def __init__(self):
        self.mutex.acquire()
        try:
            if not isfile(self.PROTOCOL_LOCATION):
                with open(self.PROTOCOL_LOCATION, "w+") as fd:
                    fd.close()
        finally:
            self.mutex.release()

    def load(self):
        self.mutex.acquire()
        try:
            with open(self.PROTOCOL_LOCATION, "r+") as fd:
                ret = fd.read()
                fd.close()
        finally:
            self.mutex.release()
            return ret

    def reset(self):
        self.mutex.acquire()
        try:
            print('Deleting save')
            remove(self.PROTOCOL_LOCATION)
        finally:
            self.mutex.release()
            
    def print(self, line):
        self.mutex.acquire()
        try:
            with open(self.PROTOCOL_LOCATION, "a+") as fd:
                line.strip('\n')
                fd.write(line + '\n')  
                fd.close()
        finally:
            self.mutex.release()
