import os
from os import listdir
from os.path import isfile, join

dir = "Parrot_Bebop/"

files = onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

counter = 1
for f in files:
    extension= f.split(".")[-1]
    path = dir + f
    newFile = dir + "sample{}.{}".format(str(counter).zfill(5), extension)
    counter += 1
    os.rename("{}{}".format(dir,f), newFile)
    # print(newFile)