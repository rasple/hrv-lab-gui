from os.path import isfile
from os import remove
from threading import Thread, Lock

class Log:

    
    LOG_LOCATION='log.txt'
    mutex = Lock()

    def __init__(self):
        self.mutex.acquire()
        try:
            if not isfile(self.LOG_LOCATION):
                with open(self.LOG_LOCATION, "w+") as fd:
                    fd.close()
        finally:
            self.mutex.release()

    def load(self):
        self.mutex.acquire()
        try:
            with open(self.LOG_LOCATION, "r+") as fd:
                ret = fd.read()
                fd.close()
        finally:
            self.mutex.release()
            return ret

    def reset(self):
        self.mutex.acquire()
        try:
            print('Deleting save')
            remove(self.LOG_LOCATION)
        finally:
            self.mutex.release()
    def append(self, line):
        self.mutex.acquire()
        try:
            with open(self.LOG_LOCATION, "a+") as fd:
                line.strip('\n')
                fd.write(line + '\n')  
                fd.close()
        finally:
            self.mutex.release()
            