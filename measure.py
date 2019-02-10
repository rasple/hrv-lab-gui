import datetime
import urllib.request as urlget
from random import randint
from threading import Timer
from timeit import default_timer
from log import Log
from protocol import Protocol
from settings import Settings
from timetools import convert_seconds_to_time, convert_time_to_seconds


class Measurement:

    running = False
    start_time = 0
    turn_on = None
    turn_off = None
    final = None
    result = ""
    

    

    def turn_pi(self, state):
        l = Log()
        if state == 'on':
            l.print('Turning Pi on')
            res = ""
            try:
                res = urlget.urlopen('http://' + Settings().get('raspi_ip') + ':31415/?action=on', timeout=1).getcode()
                l.print('Pi response: ' + res)
                l.print('Successful!')
            except:
                l.print('Pi did not respond')
                #self.abort()   
        else:
            l.print('Turning Pi off')
            try:
                res = urlget.urlopen('http://' + Settings().get('raspi_ip') + ':31415/?action=off', timeout=1).getcode()
                l.print('Pi response: ' + res)
                l.print('Successful!')
            except:
                l.print('Pi did not respond')
                #self.abort()
                

    def turn_dect(self, state):
        l = Log()
        if state == 'on':
            l.print('Turning DECT on')
            try:
                res = urlget.urlopen('http://' + Settings().get('dect_ip') + '/sw?u=admin&p=admin&o=1&f=on',timeout=1).getcode()
                l.print('DECT response: ' + res)
                l.print('Successful!')
            except:
                l.print('DECT did not respond')
                #self.abort()
            
        else:
            l.print('Turning DECT off')
            try:
                res = urlget.urlopen('http://' + Settings().get('dect_ip') + '/sw?u=admin&p=admin&o=1&f=off', timeout=1).getcode()
                l.print('DECT response: ' + res)
                l.print('Successful!')
            except:
                l.print('DECT did not respond')
                #self.abort()
                
    def kill(self):
        Log().print('Turning off all devices')
        self.turn_dect('off')
        self.turn_pi('off')
    
    def on(self, start):
        l = Log()
        message = 'Radiation on after ' + convert_seconds_to_time(start) + ' (at ' + datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y') + ')\n'
        self.result += message
        l.print(message)
        self.turn_pi('on')
        self.turn_dect('on')

    def off(self, stop):
        l = Log()
        message = 'Radiation off after ' + convert_seconds_to_time(stop) + '(at ' + datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y') + ')\n'
        self.result += message
        l.print(message)
        self.turn_pi('off')
        self.turn_dect('off')

    def get_time(self):
        s = Settings()
        if not self.running:
            return s.get('total_time')
        else:
            return convert_seconds_to_time(convert_time_to_seconds(s.get('total_time')) - (int(default_timer()) - int(self.start_time)))

    def cancel(self):
        if self.turn_off != None and self.turn_on != None and self.final != None:
            self.turn_on.cancel()
            self.turn_off.cancel()
            self.final.cancel()

    def start(self):
        if self.turn_off != None and self.turn_on != None and self.final != None:
            self.turn_on.start()
            self.turn_off.start()
            self.final.start()

    def abort(self):
        self.cancel()
        self.kill()
        self.running = False
        message = 'Aborted: ' + datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        Protocol().print(message)
        Log().print(message)

    def start_measurement(self, form):
        
        self.cancel()

        p = Protocol()
        l = Log()
        s = Settings()
        self.running = True
        time = datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        self.start_time = default_timer()

        l.print('Starting Measurement')
        self.result += 'Begin: ' + time + '\n'
        self.result = ('Age: ' + form['age'] + '\n' +
            'Sex: ' + form['sex'] + '\n' +
            'Weight: ' + form['weight'] + '\n' +
            'Height: ' + form['height'] + '\n' +
            'Start time: ' + str(time) + '\n')

        PRE_WAIT_TIME = convert_time_to_seconds(s.get('pre_wait_time'))
        POST_WAIT_TIME = convert_time_to_seconds(s.get('post_wait_time'))
        RADIATION_TIME = convert_time_to_seconds(s.get('radiation_time'))
        TOTAL_TIME = convert_time_to_seconds(s.get('total_time'))
        
        window = TOTAL_TIME - PRE_WAIT_TIME - POST_WAIT_TIME - RADIATION_TIME

        start = PRE_WAIT_TIME + randint(0, window)

        end = start + RADIATION_TIME

        self.turn_on = Timer(float(start), self.on, [start])
        self.turn_off = Timer(float(end), self.off, [end])
        self.final = Timer(float(TOTAL_TIME), self.end)
        
        self.start()

    def end(self):
        self.cancel()
        self.kill()
        self.running = False
        Protocol().print(self.result)
        time = datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        Protocol().print('End: ' + time)
        Log().print('Measurement ended')
