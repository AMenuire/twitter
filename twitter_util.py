from collections import Counter
from wordcloud import WordCloud
import multidict as multidict
import matplotlib.pyplot as plt

def path_to_image_html(path):
    '''
     This function essentially convert the image url to 
     '<img src="'+ path + '"/>' format. And one can put any
     formatting adjustments to control the height, aspect ratio, size etc.
     within as in the below example. 
    '''
    #return '<blockquote class="twitter-tweet"><a href="https://twitter.com/x/status/807811447862468608"></a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>' 
    return '<img src="'+ path + '" style=max-height:124px;"/>'
    
def path_to_embedded_tweet(path):
    '''
     This function essentially convert the image url to 
     '<img src="'+ path + '"/>' format. And one can put any
     formatting adjustments to control the height, aspect ratio, size etc.
     within as in the below example. 
    '''
    return '<blockquote class="twitter-tweet"  data-cards="hidden"><a href="https://twitter.com/x/status/'+ str(path) + '"></a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8" ></script>' 
    #return '<img src="'+ path + '" style=max-height:124px;"/>'
	
	
def top_words(df,column):
	c = Counter(" ".join(df[column].astype(str)).split())
	ignore = ['de','la','le','RT','sur','du', 'la']
	for word in c :
		if len(word) < 6 or word[0] == "#" or word[0] == "@":
			ignore.append(word)
	for word in ignore :
		if word in c:
			del c[word]
	most_common_words = c.most_common(100)
	return most_common_words

def top_hashtags(df,column):
	d = Counter(" ".join(df[column].astype(str)).split())
	ignore = []
	for word in d :
		if not word[0] == '#':
			ignore.append(word)
	for word in ignore :
		if word in d :
			del d[word]
	most_common_hashtags = d.most_common(50)
	return most_common_hashtags
	
def generate_cloud(most_common_words):
	fullTermsDict = multidict.MultiDict()
	for word in most_common_words:
		fullTermsDict.add(word[0], word[1])
	wc = WordCloud(background_color="white", max_words=1000)
	# generate word cloud
	wc.generate_from_frequencies(fullTermsDict)
	# show
	plt.imshow(wc, interpolation="bilinear")
	plt.axis("off")
	plt.show()