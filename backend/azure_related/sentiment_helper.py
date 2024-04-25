import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Set up the Azure Text Analytics client
text_analytics_key = os.environ.get('LANGUAGE_KEY')
text_analytics_endpoint = os.environ.get('LANGUAGE_ENDPOINT')

credential = AzureKeyCredential(text_analytics_key)
text_analytics_client = TextAnalyticsClient(endpoint=text_analytics_endpoint, credential=credential)

def perform_sentiment_analysis(text):
    documents = [text]
    response = text_analytics_client.analyze_sentiment(documents=documents)[0]
    print("response: {}".format(response))
    flagged = flag_sentences(response)
    
    sentiment = response.sentiment
    confidence_scores = {
        "positive": response.confidence_scores.positive,
        "neutral": response.confidence_scores.neutral,
        "negative": response.confidence_scores.negative
    }
    
    print("flagged: {}".format(flagged))

    return flagged


def flag_sentences(response):
    flags = []
    for sentence in response.sentences:
        if sentence.sentiment == 'negative' and sentence.confidence_scores.negative >= 0.85:
            flags.append(sentence)
    return flags

perform_sentiment_analysis("Like I, you know, it's so disruptive to my life.")