import boto3

client = boto3.client('translate', region_name="us-east-2")
text = "Hola mi nombre es Kito"
result = client.translate_text (Text=text, SourceLanguageCode="auto", TargetLanguageCode="en") #auto detect the language source 
print (result['TranslatedText'])
