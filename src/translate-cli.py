import boto3
import click

@click.command()
@click.option('--phrase', prompt='Put in a phrase in any language to translate', help='This is a tool that translates text')

def action (phrase):
    client = boto3.client('translate', region_name="us-east-2")
    click.echo(click.style(f"Translate phrase: {phrase}", fg='red'))
    result = client.translate_text (Text=phrase, SourceLanguageCode="auto", TargetLanguageCode="en") #auto detect the language source 
    text = (result['TranslatedText'])
    click.echo(click.style(f'{text}', bg='blue', fg='white'))
    
if __name__=='__main__':
    action()