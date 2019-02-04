def convert_time_to_seconds(time):
    [minutes, seconds] = time.split(':')
    return int(minutes) * 60 + int(seconds)

def convert_seconds_to_time(seconds):
    minutes = int(seconds / 60)
    remaining_seconds = int(seconds % 60)
    return "{0:02d}:{1:02d}".format(minutes, remaining_seconds)
