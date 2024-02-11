import math

def hours_minutes(seconds):
    hours = math.ceil(seconds/3600)
    minutes = math.ceil(seconds/60 % 60)
    return  str(hours) + ":" + str(minutes).zfill(2)

print(hours_minutes(3900))
