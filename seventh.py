exp-7
Text Analytics
1. Extract Sample document and apply following document preprocessing methods:
Tokenization, POS Tagging, stop words removal, Stemming and Lemmatization.
2. Create representation of document by calculating Term Frequency and Inverse Document
Frequency.

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# 1. Sample Document
text = "The quick brown foxes are jumping over the lazy dogs. They love jumping!"

# Tokenization
tokens = word_tokenize(text.lower()) # converting to lower case is standard
print("Tokens:", tokens)

# POS Tagging
pos_tags = nltk.pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

# Stop Words Removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w not in stop_words and w.isalnum()]
print("\nFiltered Tokens (No Stop Words):", filtered_tokens)

# Stemming
ps = PorterStemmer()
stemmed = [ps.stem(w) for w in filtered_tokens]
print("\nStemmed Words:", stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in filtered_tokens]
print("\nLemmatized Words:", lemmatized)

# 2. TF-IDF Representation
sample_docs = [
    "The quick brown fox jumps",
    "The lazy dog sleeps",
    "The fox is quick and the dog is lazy"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sample_docs)

# Create a readable table for TF-IDF
df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print("\n--- TF-IDF Representation ---")
print(df_tfidf)
