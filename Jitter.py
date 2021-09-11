#JITTER CALCULATION USING PYTHON


#Jitter function in python
def absolute_jitter(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    absolute_jitter = call(pointprocess, "Get jitter (local, absolute)", 0, 0, 0.0001, 0.02, 1.3)
    return (util.format_output(absolute_jitter, 6) + "s")
#Jitter_percentage function in python
def jitter_percentage(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    jitter_percentage = call(pointprocess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    return (util.format_output(jitter_percentage) + "%")
#Jitter_rap function in python
def relative_average_perturbation(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    rapJitter = call(pointprocess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    return (util.format_output(rapJitter) + "%")
#Jitter_ppq5 function in python
def pitch_period_perturbation(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    ppq5Jitter = call(pointprocess, "Get jitter (ppq5)", 0, 0, 0.0001, 0.02, 1.3)
    return (util.format_output(ppq5) + "%")
