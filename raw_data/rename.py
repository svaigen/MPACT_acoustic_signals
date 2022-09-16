import os
from os import listdir
from os.path import isfile, join

dirs = ['DJI_Inspire1Pro/','DJI_Matrice100/','DJI_Matrice600/','DJI_Phantom3/','DJI_Phantom4Pro/','Parrot_AR/','Parrot_Bebop/']

for dir in dirs:
    files = onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

    # counter = 1
    for f in files:
        if 'sample' not in f:
            continue
        end = f.split("sample")[-1]
        if len(end) > 9:
            path = dir + f
            end = end[1:]
            newFile = dir + "sample{}".format(str(end))
            # counter += 1
            os.rename("{}{}".format(dir,f), newFile)
            # print(newFile)