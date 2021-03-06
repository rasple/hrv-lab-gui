from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    send_from_directory,
    url_for,
    Response,
)
from platform import system as system_name
from subprocess import call as system_call
import os
from settings import Settings
from json import dumps
import measure
from log import Log
from protocol import Protocol
from threading import Thread
from measure import Measurement
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

m = Measurement()


@app.route('/')
def main_page():
    return render_template('lab.html')


# Templates


@app.route('/settings', methods=('GET', 'POST'))
def settings_page_save():
    if request.method == 'GET':
        return render_template('settings.html', settings=Settings().load())
    else:
        Settings().write(**request.form)
        return render_template('settings.html', settings=Settings().load())


@app.route('/reset')
def reset_settings():
    print('reseting')
    Settings().reset()
    return render_template('settings.html', settings=Settings().load())


@app.route('/imprint')
def imprint_page():
    return render_template('imprint.html')


@app.route('/information')
def information_page():
    return render_template('information.html')


@app.route('/start', methods=['POST'])
def start():
    global m
    m.start_measurement(request.form)
    return Response(status=200)


@app.route('/abort')
def abort():
    m.abort()
    return Response(status=200)


@app.route('/time')
def time():
    global m
    return jsonify({'time': m.get_time(), 'running': m.running})


@app.route('/log')
def get_log():
    return Log().load()


@app.route('/clearLog')
def clear_log():
    Log().reset()
    return Response(status=200)


@app.route('/protocol')
def protocol():
    return Protocol().load()


@app.route('/clearProtocol')
def clear_protocol():
    Protocol().reset()
    return Response(status=200)

@app.route('/running')
def running():
    return m.running

@app.route('/ping')
def ping_response():
    return jsonify(
        {
            'raspi': ping(Settings().load()['raspi_ip']['value']),
            'dect': ping(Settings().load()['dect_ip']['value'])
        }
    )


def ping(host):
    param = ' -n 1 -w 1000 ' if system_name().lower() == 'windows' else ' -c 1 -W 1 '
    #command = ['ping', param, host]
    command = 'ping' + param + host
    return system_call(command) == 0

if __name__== '__main__':
    app.run(host='0.0.0.0', port=80)
