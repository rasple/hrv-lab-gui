from json import dumps, loads
from os.path import isfile
from os import remove

class Settings:

    SETTINGS_LOCATION='settings.conf'

    def __init__(self):
        if isfile(self.SETTINGS_LOCATION):    
            with open(self.SETTINGS_LOCATION, "r+") as fd:
                fd.seek(0)
                if fd.read() == "":
                    fd.close()
                    self.write()
                else:
                    fd.close()
        else:
            with open(self.SETTINGS_LOCATION, "w+") as fd:
                fd.close()
                self.write()

    def load(self):
        with open(self.SETTINGS_LOCATION, "r+") as fd:
            ret = loads(fd.read())
            fd.close()
        return ret

    def reset(self):
        print('Deleting save')
        remove(self.SETTINGS_LOCATION)

    def write(
        self,
        raspi_ip="192.168.0.15",
        dect_ip="192.168.0.17",
        pre_wait_time_in_s='03:00',
        post_wait_time_in_s='03:00',
        total_time_in_s='15:00',
        radiation_time='05:00',
    ):

        with open(self.SETTINGS_LOCATION, "w+") as fd:
            fd.write(
                dumps(
                    {
                        "raspi_ip": {
                            "value": raspi_ip,
                            "name": "IP adress of Raspberry Pi",
                            "tooltip": "The IP adress of the Raspberry PI",
                            "type": "text",
                            "pattern": "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        },
                        "dect_ip": {
                            "value": dect_ip,
                            "name": "IP adress of DECT Station",
                            "tooltip": "The IP of the DECT Station",
                            "type": "text",
                            "pattern": "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
                        },
                        "pre_wait_time_in_s": {
                            "value": pre_wait_time_in_s,
                            "name": "Pre-Measurement time",
                            "tooltip": "Time before the actual radiation exposure where nothing happens",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$"
                        },
                        "post_wait_time_in_s": {
                            "value": post_wait_time_in_s,
                            "name": "Post-Measurement time",
                            "tooltip": "Time after the actual radiation exposure where nothing happens",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$"
                        },
                        "radiation_time": {
                            "value": radiation_time,
                            "name": "Radiation time",
                            "tooltip": "Amount of seconds of actual radiation",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$"
                        },
                    }
                )
            )
            fd.truncate()
            fd.close()

