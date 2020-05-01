from nltk.classify import NaiveBayesClassifier, accuracy
from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
from nltk_example.stopwords import stopwords
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')


def tweets_features(tweet):
    tweet = remove_stop_words(tweet)
    return {'tweet': tweet}


def creating_set(filename):
    result_set = []
    file = open(filename, "r", encoding='utf-8')
    line = file.readline()
    first_line = line.strip('  ').split()
    for line in file:
        line = line.split('\t')
        line[-1] = line[-1][:-1]
        first_el = tweets_features(line[1])
        for i in range(2, len(line)):
            if line[i] == '1':
                second_el = first_line[i]
                result_set.append((first_el, second_el))
    return result_set


# def creating_set_2(filename):
#     result_set = []
#     file = open(filename, "r", encoding='utf-8')
#     line = file.readline()
#     first_line = line.strip('  ').split()
#     for line in file:
#         line = line.split('\t')
#         # line[-1] = line[-1][:-1]
#         first_el = tweets_features(line[0])
#         result_set.append((first_el, line[1]))
#     return result_set


def remove_stop_words(tweet):
    tokens_without_sw = ""
    # tweet = word_tokenize(tweet)
    for word in tweet.split():
        if not word.lower() in stopwords:
            tokens_without_sw += word.lower() + " "
    return tokens_without_sw


train_set = creating_set('2018-E-c-En-train.txt')

# train_set = creating_set_2('NRC-Emotion-Intensity-Lexicon-v1.txt')

devtest_set = creating_set('2018-E-c-En-dev.txt')
# print(train_set)
classifier = NaiveBayesClassifier.train(train_set)

print(accuracy(classifier, devtest_set))
label = classifier.classify(tweets_features("dont Good morning! Have a good day! amazing beautiful wonderful"))
print(label)

probabilities = classifier.prob_classify(tweets_features("doesn't Good morning! Have a good day! amazing beautiful wonderful"))

for sample in probabilities.samples():
    print("{0}: {1}".format(sample, probabilities.prob(sample)))
# errors = []
# for (tweet, tag) in devtest_set:
#     guess = classifier.classify(tweet)
#     if guess != tag:
#         errors.append((tag, guess, tweet['tweet']))
#
# for i in errors:
#     print(i)
