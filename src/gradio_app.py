import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from src.sentiment_model import classify_sentiment

def analyze_csv(file):
    try:
        df = pd.read_csv(file.name)
        if 'TweetText' not in df.columns:
            return None, None, "The uploaded CSV file must contain a column named 'TweetText'."

        df['Sentiment'] = df['TweetText'].apply(classify_sentiment)
        sentiment_counts = df['Sentiment'].value_counts()
        total_tweets = len(df)

        positive_score = round((sentiment_counts.get('Positive', 0) / total_tweets) * 100, 2)
        neutral_score = round((sentiment_counts.get('Neutral', 0) / total_tweets) * 100, 2)
        negative_score = round((sentiment_counts.get('Negative', 0) / total_tweets) * 100, 2)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(sentiment_counts.index, sentiment_counts.values, color=['red', 'blue', 'green'])
        ax.set_title("Sentiment Distribution")
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Count")
        plt.tight_layout()

        scores_dict = {
            "Positive": positive_score,
            "Neutral": neutral_score,
            "Negative": negative_score
        }
        final_sentiment = max(scores_dict, key=scores_dict.get)
        final_confidence = scores_dict[final_sentiment]

        final_prediction = f"**Final Predicted Sentiment:** {final_sentiment}\n\n**Final Confidence Level:** {final_confidence}%"

        return fig, sentiment_counts.to_dict(), final_prediction
    except Exception as e:
        return None, None, f"An error occurred: {str(e)}"

interface = gr.Interface(
    fn=analyze_csv,
    inputs=gr.File(label="Upload a CSV File"),
    outputs=[
        gr.Plot(label="Sentiment Distribution"),
        gr.JSON(label="Calculated Sentiment Data"),
        gr.Markdown(label="Final Prediction"),
    ],
    title="Real Time Sentimental Analysis of Tweets",
    description="Upload a CSV file containing tweets. The app will classify tweets into Positive, Neutral, and Negative sentiments."
)

if __name__ == "__main__":
    interface.launch()
