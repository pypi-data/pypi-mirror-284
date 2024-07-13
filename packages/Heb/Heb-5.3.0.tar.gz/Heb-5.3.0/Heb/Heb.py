import pyperclip
class Heb:
    def p5(self):
        pyperclip.copy('''
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
              
# Load the 20 newsgroups dataset (a sample dataset included in scikit-learn)
newsgroups_train = fetch_20newsgroups(subset='train')
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(newsgroups_train.data,
newsgroups_train.target, test_size=0.2, random_state=42)
# Vectorize the text data using TF-IDF representation
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
# Train Naïve Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vectorized, y_train)
# Predict using Naïve Bayes classifier
nb_predictions = nb_classifier.predict(X_test_vectorized)
              
# Train SVM classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_vectorized, y_train)
# Predict using SVM classifier
svm_predictions = svm_classifier.predict(X_test_vectorized)

# Evaluate Naïve Bayes classifier
print("Naïve Bayes Classifier:")
print(classification_report(y_test,nb_predictions,target_names=newsgroups_train.target_
names))
# Evaluate SVM classifier
print("\nSupport Vector Machine (SVM) Classifier:")
print(classification_report(y_test,svm_predictions,target_names=newsgroups_train.target
_names)) 

''')
    def p6(self):
        pyperclip.copy('''
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_20newsgroups
# Load the 20 newsgroups dataset (a sample dataset included in scikit-learn)
newsgroups = fetch_20newsgroups(subset='all')
# Vectorize the text data using TF-IDF representation
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(newsgroups.data)
# Perform K-means clustering
k = 20 # Number of clusters (you can adjust this)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
# Print top terms for each cluster
terms = vectorizer.get_feature_names()
order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
for i in range(k):
 print(f"Cluster {i + 1}:")
 top_terms = [terms[ind] for ind in order_centroids[i, :5]]
 print(top_terms)
''')
    def p7(self):
        pyperclip.copy('''

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
# Sample text
text = "John likes to play football with his friends."
# Tokenize the text
tokens = word_tokenize(text)
# Rule-based PoS tagging
def rule_based_pos_tagging(tokens):
 tagged_tokens = []
 for token in tokens:
 if token.lower() in ["john", "he", "his"]:
 tagged_tokens.append((token, 'NNP')) # Proper noun
 elif token.lower() in ["likes", "play"]:
 tagged_tokens.append((token, 'VB')) # Verb
 elif token.lower() in ["to", "with"]:
 tagged_tokens.append((token, 'TO')) # To or preposition
 elif token.lower() in ["football", "friends"]:
 tagged_tokens.append((token, 'NN')) # Noun
 else:
 tagged_tokens.append((token, 'NN')) # Default to noun
 return tagged_tokens
# Statistical PoS tagging
def statistical_pos_tagging(tokens):
 tagged_tokens = pos_tag(tokens)
 return tagged_tokens
# Remove stopwords for better accuracy in statistical PoS tagging
stop_words = set(stopwords.words('english'))
tokens_without_stopwords = [token for token in tokens if token.lower() not in stop_words]
# Perform PoS tagging
rule_based_tags = rule_based_pos_tagging(tokens)
statistical_tags = statistical_pos_tagging(tokens_without_stopwords)
# Display the results
print("Rule-based PoS tagging:")
print(rule_based_tags)
print("\nStatistical PoS tagging:")
print(statistical_tags)

''')
    def p8(self):
        pyperclip.copy('''
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.callbacks import LambdaCallback
import random
import sys
# Load and preprocess the text data
with open('text_corpus.txt', 'r', encoding='utf-8') as f:
 text = f.read().lower()
chars = sorted(list(set(text)))
char_indices = {char: i for i, char in enumerate(chars)}
indices_char = {i: char for i, char in enumerate(chars)}
max_len = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - max_len, step):
 sentences.append(text[i: i + max_len])
 next_chars.append(text[i + max_len])

x = np.zeros((len(sentences), max_len, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
 for t, char in enumerate(sentence):
 x[i, t, char_indices[char]] = 1
 y[i, char_indices[next_chars[i]]] = 1
# Define the LSTM model
model = Sequential()
model.add(LSTM(128, input_shape=(max_len, len(chars))))
model.add(Dense(len(chars), activation='softmax'))
# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam')
# Function to sample the next character
def sample(preds, temperature=1.0):
 preds = np.asarray(preds).astype('float64')
 preds = np.log(preds) / temperature
 exp_preds = np.exp(preds)
 preds = exp_preds / np.sum(exp_preds)
 probas = np.random.multinomial(1, preds, 1)
 return np.argmax(probas)
              # Function to generate text
def generate_text(seed_text, temperature=0.5, generated_text_length=400):
 generated_text = seed_text.lower()
 for i in range(generated_text_length):
 x_pred = np.zeros((1, max_len, len(chars)))
 for t, char in enumerate(seed_text):
 x_pred[0, t, char_indices[char]] = 1.
 preds = model.predict(x_pred, verbose=0)[0]
 next_index = sample(preds, temperature)
 next_char = indices_char[next_index]
 generated_text += next_char
 seed_text = seed_text[1:] + next_char
 return generated_text
# Train the model and generate text
def on_epoch_end(epoch, _):
 print()
 print('----- Generating text after Epoch: %d' % epoch)
 start_index = random.randint(0, len(text) - max_len - 1)
 for temperature in [0.2, 0.5, 1.0]:
 seed_text = text[start_index: start_index + max_len]
 generated_text = generate_text(seed_text, temperature)
 print('----- Temperature:', temperature)
 print(seed_text + generated_text)
print_callback = LambdaCallback(on_epoch_end=on_epoch_end)
# Fit the model
model.fit(x, y,
 batch_size=128,
 epochs=30,
 callbacks=[print_callback])


''')