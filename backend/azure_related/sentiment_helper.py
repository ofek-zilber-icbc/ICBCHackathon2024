import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set up the Azure Text Analytics client
text_analytics_key = os.environ.get('TEXT_KEY')
text_analytics_endpoint = os.environ.get('TEXT_ENDPOINT')

credential = AzureKeyCredential(text_analytics_key)
text_analytics_client = TextAnalyticsClient(endpoint=text_analytics_endpoint, credential=credential)

def perform_sentiment_analysis(text):
    documents = [text]
    response = text_analytics_client.analyze_sentiment(documents=documents)[0]
    
    sentiment = response.sentiment
    confidence_scores = {
        "positive": response.confidence_scores.positive,
        "neutral": response.confidence_scores.neutral,
        "negative": response.confidence_scores.negative
    }
    
    return sentiment, confidence_scores
