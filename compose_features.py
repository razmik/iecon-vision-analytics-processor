import sys
import csv
import json
import pandas as pd
from os import listdir
from os.path import join, isfile

word_list_filename = 'features/word_list.csv'
input_folder = 'data/'
output_folder = 'features/'
filenames = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

word_list = pd.read_csv(word_list_filename, nrows=1).columns.values

# compose the template word dictionary
word_dictionary_template = {}
for word in word_list:
    word_dictionary_template[word] = 0
dict_keys = list(word_dictionary_template.keys())

print('Number of files', len(filenames))

# loop through all the frames to create the features
for filename in filenames:

    if 'frame0' in filename:

        # create word features for one frame
        with open(input_folder + filename) as data_file:
            data = json.load(data_file)
            sequence_feature_list = []

            for frame in data:
                words = word_dictionary_template.copy()
                if 'tags' in frame:
                    for tag in frame['tags']:
                        words[tag['name']] += 1
                sequence_feature_list.append(words)

        # save the data on the feature
        print('Writing features of', filename)
        with open(output_folder + filename.split('.')[0] + '.csv', 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=dict_keys)
            writer.writeheader()
            for seq in sequence_feature_list:
                writer.writerow(seq)

print('Completed.')
