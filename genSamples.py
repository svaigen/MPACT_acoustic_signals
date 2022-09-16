import os
from os import listdir
from os.path import isfile, join
import pydub

fileSampleSummary = 'samples_summary.csv'
fSamplesSummary = open(fileSampleSummary,'w')
fSamplesSummary.write("Model; Number of Samples\n")

fileSampleMap = 'samples_map.csv'
fSamplesMap = open(fileSampleMap,'w')
fSamplesMap.write("Sample File; Origin File\n")

outputDir = "samples/"
dirs = ['raw_data/DJI_Inspire1Pro/','raw_data/DJI_Matrice100/','raw_data/DJI_Matrice600/','raw_data/DJI_Phantom3/','raw_data/DJI_Phantom4Pro/','raw_data/Parrot_AR/','raw_data/Parrot_Bebop/']

models = {
    'raw_data/DJI_Inspire1Pro/': 'insp1pro_',
    'raw_data/DJI_Matrice100/': 'mat100_',
    'raw_data/DJI_Matrice600/': 'mat600_',
    'raw_data/DJI_Phantom3/': 'phant3_',
    'raw_data/DJI_Phantom4Pro/': 'phant4pro_',
    'raw_data/Parrot_AR/': 'ar_',
    'raw_data/Parrot_Bebop/': 'beb_'
    }

dbms = [-40, -30, -20, -10, 0, 10, 20]
# maxDbm = -9999999999999
# minDbm = 9999999999999

for dir in dirs:
    files = onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
    indexSample = 0
    for f in files:
        if 'sample' not in f:
            continue
        fullF = "{}{}".format(dir,f)
        extension = f.split(".")[-1]
        sound_file = ''
        if extension == "mp3":
            sound_file = pydub.AudioSegment.from_mp3(fullF)
        else:
            sound_file = pydub.AudioSegment.from_wav(fullF)
        
        range = 1000
        current = 0
        while( (current+range) < len(sound_file)):
            sample = sound_file[current : (current + range)]
            # print("original dbm: {}".format(sample.max_dBFS))
            for dbm in dbms:
                dbmChange = dbm - sample.max_dBFS
                newSound = sample.apply_gain(dbmChange)
                name = "samples/{}/{}_{}_{}dbm.mp3".format(models[dir][:-1],models[dir][:-1],str(indexSample).zfill(5),str(dbm).zfill(2))
                newSound.export(name, format="mp3")
                fSamplesMap.write("{};{}\n".format(name,fullF))
            current = current + range
            # print(fullF, str(indexSample).zfill(5), sample.max_dBFS)
            indexSample += 1
            # if (maxDbm < sample.max_dBFS):
            #     maxDbm = sample.max_dBFS
            # if (minDbm > sample.max_dBFS):
            #     minDbm = sample.max_dBFS
        #including the last part:
        sample = sound_file[current : ]
        if(len(sample) > 0):
            # print("{} {} {} (last)".format(fullF,str(indexSample).zfill(5), sample.max_dBFS))
            sample = sound_file[current : (current + range)]
            # print("original dbm: {}".format(sample.max_dBFS))
            for dbm in dbms:
                dbmChange = dbm - sample.max_dBFS
                newSound = sample.apply_gain(dbmChange)
                name = "samples/{}/{}_{}_{}dbm.mp3".format(models[dir][:-1],models[dir][:-1],str(indexSample).zfill(5),str(dbm).zfill(2))
                newSound.export(name, format="mp3")
                fSamplesMap.write("{};{}\n".format(name,fullF))
            current = current + range
            indexSample += 1
            # if (maxDbm < sample.max_dBFS):
            #     maxDbm = sample.max_dBFS
            # if (minDbm > sample.max_dBFS):
            #     minDbm = sample.max_dBFS
    fSamplesSummary.write("{};{}\n".format(models[dir][:-1],indexSample))

# print("Max Dbm: {} | Mini Dbm: {}".format(maxDbm, minDbm))
fSamplesSummary.close()
fSamplesMap.close()