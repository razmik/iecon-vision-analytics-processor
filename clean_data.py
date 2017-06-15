import json
from os import listdir
from os.path import join, isfile

input_folder = 'C:\\Users\\19146404\PycharmProjects\iecon-vision-analytics-processor/data/'.replace('\\', '/')

for filename in [f for f in listdir(input_folder) if isfile(join(input_folder, f))]:

    cleaned_data = None
    with open(input_folder + filename) as data_file:
        data = json.load(data_file)

        if len(data) > 44:
            cleaned_data = data[-44:]

    if cleaned_data is not None:
        with open(input_folder + filename, "w", encoding="utf8") as outfile:
            json.dump(cleaned_data, outfile)
            print('Updated', filename)

print('completed')