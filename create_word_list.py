import json
import csv
from os import listdir
from os.path import join, isfile
from nltk.corpus import stopwords

print('Initializing bag of words composer.')

# read input command
input_folder = 'C:\\Users\\19146404\PycharmProjects\iecon-vision-analytics-processor/data/'.replace('\\', '/')
outputfile = 'features\word_list.csv'.replace('\\', '/')

word_list = []

for filename in [f for f in listdir(input_folder) if isfile(join(input_folder, f))]:
    if 'frame0' in filename:
        with open(input_folder + filename) as data_file:
            data = json.load(data_file)

            for frame in data:
                if 'tags' in frame:
                    for tag in frame['tags']:
                        word_list.append(tag['name'])

                        # if 'categories' in frame:
                        #     for cat in frame['categories']:
                        #         word_list += list(filter(lambda a: a != '', cat['name'].split('_')))
                        #
                        # if 'description' in frame:
                        #     word_list += frame['description']['captions'][0]['text'].split()
                        #     for tag in frame['description']['tags']:
                        #         word_list.append(tag)

# remove stop words and duplicates
print('\nWord list:', len(word_list))
print(word_list)

word_list = list(set(word_list))
print('\nWord list with duplicates removed:', len(word_list))
print(word_list)

word_list = [word for word in word_list if word not in stopwords.words('english')]
print('\nWord list with stop words removed:', len(word_list))
print(word_list)

# bag_of_words_vector = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
# trained_bag_of_words = bag_of_words_vector.fit_transform(word_list).toarray()
# vocab = trained_bag_of_words.get_feature_names()

print('\nWriting to', outputfile)

f = csv.writer(open(outputfile, "w+", newline='', encoding="utf-8"))
f.writerow(word_list)
