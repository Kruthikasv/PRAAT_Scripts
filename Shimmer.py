#SHIMMER CALCULATION USING PYTHON

Shimmer function in python
def shimmer(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    localshimmer = call(sound, pointprocess, "Get shimmer (local_dB)”, 0, 0, 0.0001, 0.02, 1.3, 1.6)
    return (util.format_output(localshimmer, 6) + “dB”)

Shimmer_percentage function in python
def shimmer_percentage(file_name=None):
    sound = parselmouth.Sound(file_name)
    pointprocess = call(sound, "To PointProcess (periodic, cc)", 75, 600)
    shimmer_percentage = call(sound, pointprocess, "Get shimmer (local)”, 0, 0, 0.0001, 0.02, 1.3, 1.6)
    return (util.format_output(shimmer_percentage) + “%”)
