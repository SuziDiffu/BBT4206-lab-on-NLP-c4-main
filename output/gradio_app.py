
# gradio_app.py
import re
import joblib
import gradio as gr

# Load models
lda = joblib.load("output/lda_model.joblib")
vectorizer = joblib.load("output/vectorizer.joblib")
topics = [['practical', 'data', 'bi', 'business', 'real', 'lab', 'theory', 'like', 'tools', 'real world', 'topics', 'world'], ['labs', 'time', 'content', 'unit', 'topics', 'work', 'lab', 'opinion', 'quizzes', 'think', 'time series', 'series'], ['slides', 'liked', 'labs', 'lecture', 'content', 'number', 'learning', 'better', 'work', 'notes', 'number slides', 'bi'], ['data', 'practical', 'labs', 'unit', 'tools', 'matter', 'enjoyed', 'detailed', 'world', 'real world', 'engaging', 'opinion'], ['lab', 'assignments', 'content', 'work', 'group', 'practical', 'okay', 'like', 'topics', 'notes', 'module', 'labs'], ['topics', 'labs', 'think', 'end', 'topic', 'practical', 'understanding', 'real', 'business', 'class', 'course', 'understand']]  # List of topic names

POS = ['clear', 'engaging', 'enjoy', 'enjoyed', 'excellent', 'good', 'great', 'helpful', 'interactive', 'like', 'liked', 'practical', 'relevant', 'well']  # Positive lexicon
NEG = ['boring', 'confusing', 'delay', 'difficult', 'hard', 'insufficient', 'lack', 'late', 'not', 'poor', 'problem', 'unclear']  # Negative lexicon

def clean_text(s):
    s = str(s).lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def lex_sentiment(text):
    toks = text.split()
    score = sum(1 for t in toks if t in POS) - sum(1 for t in toks if t in NEG)
    return score

def predict(text):
    text = clean_text(text)
    bow = vectorizer.transform([text])
    topic_id = lda.transform(bow)[0].argmax()
    topic = topics[topic_id]  # Runtime lookup
    sentiment_score = lex_sentiment(text)
    return f"Topic: {topic}, Sentiment: {sentiment_score}"

iface = gr.Interface(fn=predict, inputs="text", outputs="text")
iface.launch()
