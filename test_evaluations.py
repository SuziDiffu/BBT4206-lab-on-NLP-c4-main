import pandas as pd
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download NLTK resources (if running first time)
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# Load your previously trained LDA and vectorizer
lda = joblib.load('lda_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# Initialize preprocessing tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

# Preprocessing function
def preprocess(text):
    text = str(text).lower()                       # Lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)       # Remove punctuation and numbers
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return ' '.join(tokens)

# Sentiment function
def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score > 0.05:
        return 'positive'
    elif score < -0.05:
        return 'negative'
    else:
        return 'neutral'

# New student evaluations
new_evaluations = [
    "The lecturer explains concepts clearly but the workload is too heavy.",
    "I loved the practical examples and case studies in this course!",
    "The course content was confusing and not well structured."
]

# Show top words per topic for interpretation
print("Topics and their top words:")
for i, topic_dist in enumerate(lda.components_):
    top_words = [vectorizer.get_feature_names_out()[j] for j in topic_dist.argsort()[-5:]]
    print(f"Topic {i}: {top_words}")
print("\nPredictions for new evaluations:\n")

# Predict topic and sentiment for each new evaluation
for eval_text in new_evaluations:
    clean_text = preprocess(eval_text)
    topic = lda.transform(vectorizer.transform([clean_text])).argmax()
    sentiment = get_sentiment(eval_text)  # Use original text for VADER
    print(f"Original Evaluation: {eval_text}")
    print(f"Cleaned Evaluation: {clean_text}")
    print(f"Predicted Topic: {topic}")
    print(f"Predicted Sentiment: {sentiment}")
    print("-"*50)
