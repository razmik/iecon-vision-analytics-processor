import importlib
from os import listdir
from os.path import join, isdir
import numpy as np
from time import sleep
import sys

analyzer = importlib.import_module('video_analyzer').getAnalyzer()
foldername = 'C:\\Users\\19146404\Documents\Datasets\Collective Activity Dataset\ActivityDataset\\'.replace('\\', '/')
folders = [f for f in listdir(foldername) if isdir(join(foldername, f))]

for i in np.arange(30, 200, 10):

    if i < 10:
        frame = 'frame000' + str(i) + '.jpg'
    elif i < 100:
        frame = 'frame00' + str(i) + '.jpg'
    else:
        frame = 'frame0' + str(i) + '.jpg'

    print('Start of sequence', frame)

    filenames = []
    for folder in folders:
        filenames.append(foldername + folder + '/' + frame)

    print(filenames)
    sys.exit(0)

    result = analyzer.start_process(frame, filenames, '52b05c830201461da09688253629ecd3', 'e9b3a0491efc46a8b29a3c48ab098f07',
                           False, False)

    if not result:
        print('End of sequence due to break at', frame)
        break

    print('End of frame sequence. Sleeping for 25 seconds.')
    sleep(20)

print('Operation completed.')
