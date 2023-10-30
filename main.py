from textblob import TextBlob 
from newspaper import Article

/*sentiment analysis on articles from the internet*/

url = 'input url here'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary()
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity_# -1 to 1 
print(sentiment)



from textblob import TextBlob

/*sentiment analysis on articles from our own text 'mytext.txt'*/

with open('mytext.txt', 'r') as f:
    text = f.read()
    
blob = TextBlob(text)
sentiment = blob.sentiment.polarity_# -1 to 1 
print(sentiment)