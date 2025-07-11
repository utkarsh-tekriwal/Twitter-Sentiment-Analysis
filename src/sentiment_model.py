from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

roberta = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(roberta)
model = AutoModelForSequenceClassification.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']

def preprocess_tweet(tweet):
    tweet_words = []
    for word in tweet.split():
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word = "http"
        tweet_words.append(word)
    return " ".join(tweet_words)

def classify_sentiment(tweet):
    tweet_proc = preprocess_tweet(tweet)
    encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')
    output = model(**encoded_tweet)
    scores = softmax(output[0][0].detach().numpy())
    max_score_idx = scores.argmax()
    return labels[max_score_idx]
