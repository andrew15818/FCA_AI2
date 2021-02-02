# -*- coding: utf8 -*-
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from pandas import DataFrame
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB


def load_data(filename='mail.txt'):
 # A DataFrame is like a giant array, with class and message categories
    data = DataFrame(columns=['class', 'message'])
    lines = []
    with open(filename, 'r') as f:
        # Split every line into the message and it's class
        lines = f.readlines()
        lines = [line.split('\t') for line in lines]
    # Make an array for easier processing later
    data  = DataFrame(lines, columns=['class', 'message'])

    return data

def main():
    data = load_data()

    # A vectorizer will remove punctuation from our strings,
    # and count how many times a word appears
    # This makes it harder to fool our system by adding symbols
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(data['message'].values)

    # Get the answers to use for training
    targets = data['class'].values
    
    # Our classifier now knows which words appear in spam and ham messages
    classifier = MultinomialNB()
    classifier.fit(counts, targets)

    # Time to try it on some new messages!
    test_data = load_data(filename='test_messages.txt')

    # make the format similar to our training_data
    test_labels = test_data['class'].values
    test_data_vec   = vectorizer.transform(test_data['message'].values)

    # See what our model thinks the test messages are
    preds = classifier.predict(test_data_vec)
    correct = 0

    # Print the correct answer and our guess 
    for i, data in enumerate(test_data['message']):
        print('======')
        print(f'Msg {i}:\n {data}')
        print(f'\tActual answer: {test_labels[i]} Our Guess: {preds[i]}')
        if test_labels[i] == preds[i]:
            correct += 1
        print('======\n')

    if correct == len(test_labels):
        print('Congratulations! We got all the messages right!')
    else:
        print(f'***We got {correct} out of {len(test_labels)} correct.***')
        
if __name__ == '__main__':
    main()