import json
import boto3

def lambda_handler(event, context):
    """Uses AWS Comprehend to Create Sentiments on a DataFrame"""
    comprehend = boto3.client(service_name="comprehend")
    text = event.get("text",None)
    payload = comprehend.detect_sentiment(Text=text, LanguageCode="en")
    sentiment = payload["Sentiment"]
    
    return {
        'statusCode': 200,
        'body': json.dumps('Sentiment from Lambda!'),
        'text':text,
        'sentiment': sentiment
    }
