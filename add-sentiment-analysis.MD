# Using Sentiment Libraries in Word Clouds 📚

## Why Would You Want to Use Sentiment Analysis in Word Clouds?

**Sentiment analysis in word clouds helps visualize not just the frequency of words, but also their emotional tone**, making it great for:

- **Customer Reviews**: Highlight positive and negative feedback visually.
- **Social Media Sentiment**: Analyze emotional trends in tweets or posts.
- **Survey Responses**: Understand what people feel about a product or service.

## How Words Are Classified

Word clouds do not inherently know whether a word is positive or negative. To add sentiment analysis, you need specialized libraries that classify words based on pre-trained sentiment data.

## Popular Sentiment Libraries 📖

```python
# VADER (Valence Aware Dictionary and sEntiment Reasoner)
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# TextBlob
from textblob import TextBlob
```

## Example Usage of Sentiment Libraries

### VADER Example:

```python
# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Analyze text
text = "I love this movie! It's amazing!"
scores = analyzer.polarity_scores(text)

print(scores)
# Output: {
#   'compound': 0.876,  # Overall sentiment score
#   'pos': 0.706,      # Positive score
#   'neu': 0.294,      # Neutral score
#   'neg': 0.0         # Negative score
# }
```

## Adding Sentiment to Word Clouds 🌥️

You can combine sentiment analysis with word clouds to show not only the frequency of words but also their emotional tone through color.

### Simplified Implementation:

```python
from wordcloud import WordCloud
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def create_sentiment_cloud(text):
    analyzer = SentimentIntensityAnalyzer()

    # Color function based on sentiment
    def color_func(word, **kwargs):
        score = analyzer.polarity_scores(word)['compound']
        if score > 0.5:
            return "green"     # Positive
        elif score > 0:
            return "lightgreen"  # Slightly positive
        elif score < -0.5:
            return "red"       # Negative
        elif score < 0:
            return "pink"      # Slightly negative
        return "gray"          # Neutral

    # Generate word cloud
    return WordCloud(color_func=color_func, width=800, height=400).generate(text)
```

## Context Understanding in Sentiment Analysis

Modern sentiment libraries understand:

1. **Negations**:

```python
"This is good"              # Positive
"This is not good"          # Negative
"This is not at all good"   # Very Negative
```

2. **Intensifiers**:

```python
"Good"              # Positive
"Very good"         # More Positive
"Extremely good"    # Most Positive
```

3. **Emojis**:

```python
"This movie was great! 😊"  # Positive
"This movie was great 👎"   # Mixed/Negative
```

## When to Use Each Sentiment Library

- **VADER**: Best for short texts like social media posts.
- **TextBlob**: Easy to use for general-purpose analysis.

For domain-specific needs, you can create a custom dictionary:

```python
custom_sentiment = {
    'plot twist': 0.5,
    'predictable': -0.5,
    'classic': 0.7,
    'remake': -0.2
}
```
