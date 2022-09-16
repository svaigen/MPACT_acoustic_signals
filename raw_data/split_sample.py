import pydub
# import numpy as np

sound_file = pydub.AudioSegment.from_mp3("Parrot_AR/raw00009.mp3")
# sound_file_Value = np.array(sound_file.get_array_of_samples())
ranges = [(3000,112000)]

i = 27
for x,y in ranges:
    new_file=sound_file[x : y]
    new_file.export("Parrot_AR/sample0000{}.mp3".format(i), format="mp3")
    i += 1