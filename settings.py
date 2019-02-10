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
    
    def get(self, key):
        return self.load()[key]['value']

    def write(
        self,
        raspi_ip="192.168.0.15",
        dect_ip="192.168.0.17",
        pre_wait_time='03:00',
        post_wait_time='03:00',
        radiation_time='05:00',
        total_time='15:00',
        stop_on_failure=True
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
                            "pattern": "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                            "required": True
                        },
                        "dect_ip": {
                            "value": dect_ip,
                            "name": "IP adress of DECT Station",
                            "tooltip": "The IP of the DECT Station",
                            "type": "text",
                            "pattern": "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                            "required": True
                        },
                        "total_time": {
                            "value": total_time,
                            "name": "Total time",
                            "tooltip": "Total time of measurement (minutes)",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$",
                            "required": True
                        },
                        "pre_wait_time": {
                            "value": pre_wait_time,
                            "name": "Pre-Measurement time",
                            "tooltip": "Time before the actual radiation exposure where nothing happens (minutes)",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$",
                            "required": True
                        },
                        "post_wait_time": {
                            "value": post_wait_time,
                            "name": "Post-Measurement time",
                            "tooltip": "Time after the actual radiation exposure where nothing happens (minutes)",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$",
                            "required": True
                        },
                        "radiation_time": {
                            "value": radiation_time,
                            "name": "Radiation time",
                            "tooltip": "Duration of actual radiation (minutes)",
                            "type": "text",
                            "pattern": "^\d\d:\d\d$",
                            "required": True
                        }
                    }
                )
            )
            fd.truncate()
            fd.close()

