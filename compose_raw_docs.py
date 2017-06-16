import json
from os import listdir
from os.path import join, isfile

input_folder = 'data/'
output_folder = 'raw_frames/'
filenames = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

print('Number of files', len(filenames))

# loop through all the frames to create the features
for filename in filenames:

    if 'frame0' in filename:

        # create word features for one frame
        with open(input_folder + filename) as data_file:
            data = json.load(data_file)
            raw_list = []

            for frame in data:
                raw = ''
                if 'tags' in frame:
                    for tag in frame['tags']:
                        raw += ' ' + tag['name']
                    raw_list.append(raw)

        # save the data on the feature
        print('Writing features of', filename)
        f = open(output_folder + filename.split('.')[0] + '.csv', 'w')
        for row in raw_list:
            f.write(str(row)+'\n')
        f.close()

print('Completed.')
