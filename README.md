# 🐦 Twitter Sentiment Analysis

This project classifies the sentiment of tweets using the `cardiffnlp/twitter-roberta-base-sentiment` model and visualizes them with a Gradio app.

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/gradio_app.py
```

## 📂 Input

Upload a CSV file with a column named `TweetText`.

## 📊 Output

- Sentiment Bar Chart
- JSON Stats
- Final Predicted Sentiment with Confidence

![Screenshot](assets/screenshot_2.png)
