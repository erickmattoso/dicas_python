# import nltk
# nltk.download('punkt')
# https://stackoverflow.com/questions/13965823/resource-corpora-wordnet-not-found-on-heroku
from textblob import TextBlob

text = "Today is a beautiful day" 
blob = TextBlob(text)

# Word tokenization
blob.words
"""WordList(['Today', 'is', 'a', 'beautiful', 'day'])"""

# Noun phrase extraction
blob.noun_phrases
"""WordList(['beautiful day'])"""

# sentiment analysis
blob.sentiment 
"""Sentiment(polarity=0.85, subjectivity=1.0)"""

# word counts
blob.word_counts
"""defaultdict(int, {'today': 1, 'is': 1, 'a': 1, 'beautiful': 1, 'day': 1})"""

# Spelling corection 
text = "Today is a beutiful day"
blob = TextBlob(text) 
blob.correct()
"""TextBlob("Today is a beautiful day")"""
