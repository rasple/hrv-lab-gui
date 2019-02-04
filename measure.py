from flask import g
import datetime
from settings import Settings
import urllib.request as urlget
from protocol import Protocol
from log import Log
from timetools import convert_time_to_seconds, convert_seconds_to_time
from functools import reduce
from threading import Timer
from timeit import default_timer
from random import randint


class Measurement:

    running = False
    start_time = 0
    turn_on = None
    turn_off = None
    final = None
    

    def on(self):
        time = datetime.datetime.now().isoformat()
        l = Log()
        l.print('Powering on')
        l.print(
            'Pi response: '
            + urlget.urlopen(
                'http://' + Settings().get('raspi_ip') + ':31415/?action=on'
            ).read()
        )
        l.print(
            'DECT response: '
            + urlget.urlopen(
                'http://' + Settings().get('dect_ip') + '/sw?u=admin&p=admin&o=1&f=on'
            ).read()
        )
        l.print(time)
        self.running = False

    def off(self):
        time = datetime.datetime.now().isoformat()
        l = Log()
        l.print('Powering off')
        l.print(
            'Pi response: '
            + urlget.urlopen(
                'http://' + Settings().get('raspi_ip') + ':31415/?action=on'
            ).read()
        )
        l.print(
            'DECT response: '
            + urlget.urlopen(
                'http://' + Settings().get('dect_ip') + '/sw?u=admin&p=admin&o=1&f=off'
            ).read()
        )
        l.print(time)
        self.running = False

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
        self.off()
        self.running = False
        Log().print('Aborted')

    def start_measurement(self, form):
        
        self.cancel()

        p = Protocol()
        l = Log()
        s = Settings()
        self.running = True
        time = datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        self.start_time = default_timer()

        l.print('Starting Measurement')
        p.print('Begin: ' + time)
        
        result = ('Age: ' + form['age'] + '\n' +
            'Sex: ' + form['sex'] + '\n' +
            'Weight: ' + form['weight'] + '\n' +
            'Height: ' + form['weight'] + '\n' +
            'Start time: ' + str(time) + '\n')

        PRE_WAIT_TIME = convert_time_to_seconds(s.get('pre_wait_time'))
        POST_WAIT_TIME = convert_time_to_seconds(s.get('post_wait_time'))
        RADIATION_TIME = convert_time_to_seconds(s.get('radiation_time'))
        TOTAL_TIME = convert_time_to_seconds(s.get('total_time'))
        
        # l.print('Total time: ' + str(TOTAL_TIME))
        

        window = TOTAL_TIME - PRE_WAIT_TIME - POST_WAIT_TIME - RADIATION_TIME

        start = PRE_WAIT_TIME + randint(0, window)
        end = start + RADIATION_TIME

        result += ('Start: 00:00 \n' + 
            'Radiation on: ' + convert_seconds_to_time(start) + '\n' + 
            'Radiaton off: ' + convert_seconds_to_time(end) + '\n' + 
            'End: ' + convert_seconds_to_time(TOTAL_TIME) + '\n')

        self.turn_on = Timer(float(start), self.on)
        self.turn_off = Timer(float(end), self.off)
        self.final = Timer(float(TOTAL_TIME), self.end, result)
        self.turn_on.start()
        self.turn_off.start()
        self.final.start()

    def end(self, result):
        self.cancel()
        self.off()
        self.running = False
        Protocol().print(result)
        time = datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        Protocol().print('End: ' + time)
        Log().print('Measurement ended')

