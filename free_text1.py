import wordcloud
from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt

response = requests.get('http://www.datasciencecourse.org')
root = BeautifulSoup(response.content,"lxml")
from wordcloud import WordCloud
wc = WordCloud(width=800,height=400).generate(re.sub(r"\s+"," ",root.text))
wc.to_image()
print(wc.to_image())
plt.figure()
plt.imshow(wc)
plt.show()
