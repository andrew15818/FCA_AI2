# -*- coding: utf8 -*-
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from pandas import DataFrame
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB


def load_data(filename='mail.txt'):
    # A DataFrame is like a giant array, with class and message categories


    with open(filename, 'r') as f:
        # Split every line into the message and it's class
        
       
    # Make an array for easier processing later
    

    return data

def main():
    data = load_data()

    # A vectorizer will remove punctuation from our strings,
    # and count how many times a word appears
    # This makes it harder to fool our system by adding symbols




    # Get the answers to use for training

    
    # Our classifier now knows which words appear in spam and ham messages
    


    # Time to try it on some new messages!


    # make the format similar to our training_data



    # See what our model thinks the test messages are

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