Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import boto3
... import uuid
... 
... s3 = boto3.client('s3')
... comprehend = boto3.client('comprehend')
... dynamodb = boto3.resource('dynamodb')
... table = dynamodb.Table('AnalizSonuclari')
... 
... def lambda_handler(event, context):
...     # S3'e yüklenen dosyanın bilgilerini al
...     bucket = event['Records'][0]['s3']['bucket']['name']
...     key = event['Records'][0]['s3']['object']['key']
...     
...     # Dosya içeriğini oku
...     response = s3.get_object(Bucket=bucket, Key=key)
...     text = response['Body'].read().decode('utf-8')
...     
...     # Duygu analizi yap
...     sentiment_all = comprehend.detect_sentiment(Text=text, LanguageCode='en')
...     sentiment = sentiment_all['Sentiment']
...     
...     # Sonucu DynamoDB'ye yaz
...     table.put_item(Item={
...         'FileID': str(uuid.uuid4()),
...         'FileName': key,
...         'Sentiment': sentiment,
...         'RawText': text[:100] # İlk 100 karakteri sakla
...     })
...     
