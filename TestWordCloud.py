# conding=utf-8
# ※Author = 胡志达
# ※Time = 2021/2/22 23:19
# ※File Name = TestWordCloud.py
# ※Email = 840831038@qq.com

import jieba        #分词
from matplotlib import pyplot as plt        #绘图
from wordcloud import WordCloud     #词云
from PIL import Image       #图片处理
import numpy as np      #矩阵运算
import sqlite3      #数据库
import wordcloud

conn = sqlite3.connect('movie.db')
cur = conn.cursor()
sql = "select introduction from movie250"
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
conn.close()

cut = jieba.cut(text)
string = " ".join(cut)


image = Image.open(r'C://Users/84083/Desktop/python/douban/templates/test/tree.jpg')
image_array = np.array(image)
wc = WordCloud(

    background_color='white',
    mask=image_array,
    font_path="STHUPO.TTF"
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否显示坐标轴
# plt.show()
plt.savefig(r'C://Users/84083/Desktop/python/douban/static/assets/img/word.png',dpi=500)