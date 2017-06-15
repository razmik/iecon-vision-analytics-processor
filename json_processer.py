import sys
from sklearn.feature_extraction.text import CountVectorizer
import json
import numpy as np
from nltk.corpus import stopwords

print('Initializing jsontocsv...')

# read input command
inputfile = 'data/frame0001.jpg_vision.json'
outputfile = 'vision_processed.json'

print('Reading from ' + inputfile + '...')

with open(inputfile) as data_file:
    data = json.load(data_file)

captions = []
categories = []
primary_tags = []
secondary_tags = []
for frame in data:
    if 'categories' in frame:
        for cat in frame['categories']:
            categories += list(filter(lambda a: a != '', cat['name'].split('_')))

    if 'description' in frame:
        captions += frame['description']['captions'][0]['text'].split()
        for tag in frame['description']['tags']:
            secondary_tags.append(tag)

    if 'tags' in frame:
        for tag in frame['tags']:
            primary_tags.append(tag['name'])

# remove stop words from the caption
print(captions)
captions = [word for word in captions if word not in stopwords.words('english')]
print(captions)
sys.exit(0)

"""
Creating bags of words features
"""
captions_vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
categories_vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
primary_tags_vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
secondary_tags_vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)

train_data_features_captions = captions_vectorizer.fit_transform(captions).toarray()
train_data_features_categories = categories_vectorizer.fit_transform(categories).toarray()
train_data_features_primary_tags = primary_tags_vectorizer.fit_transform(primary_tags).toarray()
train_data_features_secondary_tags = secondary_tags_vectorizer.fit_transform(secondary_tags).toarray()

vocab = captions_vectorizer.get_feature_names()
print(train_data_features_captions.shape)
print(train_data_features_categories.shape)
print(train_data_features_primary_tags.shape)
print(train_data_features_secondary_tags.shape)

sys.exit(0)

# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features_captions, axis=0)

# For each, print the vocabulary word and the number of times it
# appears in the training set
for tag, count in zip(vocab, dist):
    print(tag, count)



x = """[""" + data + """]"""

x = json.loads(x)

print('Writing to ' + outputfile + '...')

f = csv.writer(open(outputfile, "w+", newline='', encoding="utf-8"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(
    ["Age", "Author", "Date", "EmotionKeywords", "AFRAID", "ALIVE", "ANGRY", "CONFUSED", "DEPRESSED", "GOOD", "HAPPY",
     "HELPLESS", "HURT", "INDIFFERENT", "INTERESTED", "LOVE", "OPEN", "POSITIVE", "SAD", "STRONG", "Gender",
     "Timeline"])

for x in x:
    f.writerow([x["Age"],
                x["Author"],
                x["Date"],
                x["EmotionInfo"]["EmotionInfo"]["EmotionKeywords"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["AFRAID"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["ALIVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["ANGRY"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["CONFUSED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["DEPRESSED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["GOOD"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HAPPY"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HELPLESS"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["HURT"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["INDIFFERENT"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["INTERESTED"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["LOVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["OPEN"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["POSITIVE"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["SAD"],
                x["EmotionInfo"]["EmotionInfo"]["Emotions"]["STRONG"],
                x["Gender"], x["Timeline"]])

print('Successfully created the csv output file.')