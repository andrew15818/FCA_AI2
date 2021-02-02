## Lesson 9: Spam Classifier
In this project we want to identify spam email as correctly and 
accurately as possible. We can measure the types of words that 
appear in sample emails and determine from that whether or not
they are spam.

We use **Bayes' Theorem** to find the probability that an 
email is spam given the words contained in that email.

To simplify the math, we use the `sklearn` Naive Bayes classifier.
Our main job is then to format the data correctly and just pass it 
to our classifier.

For this program, we only need to run it

```python
python L9.py
```

and you should see some output on the screen.
