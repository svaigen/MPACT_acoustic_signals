import pydub
# import numpy as np

sound_file = pydub.AudioSegment.from_mp3("DJI_Inspire1Pro/raw00003.mp3")
# sound_file_Value = np.array(sound_file.get_array_of_samples())
ranges = [(5000,20000),(61000,98000),(116000,133000),(240000,260000)]

i = 
for x,y in ranges:
    new_file=sound_file[x : y]
    new_file.export("DJI_Inspire1Pro/sample0000{}.mp3".format(i), format="mp3")
    i += 1