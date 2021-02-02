import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from pandas import DataFrame
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB


def load_data(filename='mail.txt'):
 # A DataFrame is like a giant array, with class and message categories
    data = DataFrame(columns=['class', 'message'])

    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]
    data  = DataFrame(lines, columns=['class', 'message'])
    return data

def main():
    data = load_data()

    # A vectorizer will remove punctuation from our strings,
    # and count how many times a word appears
    # This makes it harder to fool our system by adding symbols
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(data['message'].values)

    targets = data['class'].values
    
    # Our classifier now knows which words appear in spam and ham messages
    classifier = MultinomialNB()
    classifier.fit(counts, targets)

    # Time to try it on some new messages!
    test_data = load_data(filename='test_messages.txt')

    # make the format similar to our training_data
    test_labels= test_data['class'].values
    test_data  = vectorizer.transform(test_data['message'].values)

    preds = classifier.predict(test_data)
    print(preds)
    # TODO: Print the results in a pleasing manner
if __name__ == '__main__':
    main()
