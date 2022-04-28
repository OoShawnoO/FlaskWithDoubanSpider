# conding=utf-8
# ※Author = 胡志达
# ※Time = 2021/2/23 13:09
# ※File Name = TestBak.py
# ※Email = 840831038@qq.com

from bs4 import BeautifulSoup
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import wordcloud
import re
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import PIL


msgbox = ''
file = open('123.txt','r+',encoding='utf-8')
for line in file.readlines():
    line = str(line)
    msgbox = msgbox+line.replace('\n','')
find_date = re.compile("[^\w]|[\d]")
onlywords = re.sub(find_date,'',msgbox)
cutwords = jieba.cut(onlywords)
cutwords_string = ' '.join(cutwords)
image = Image.open('tree.jpg')
image_array = np.array(image)
wc = WordCloud(
    background_color='white',
    scale=8,
    width = 1920,
    height = 1080,
    mask= image_array,
    font_path="STXINGKA.TTF",
)
wc.generate_from_text(cutwords_string)

fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()