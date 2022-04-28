from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/movie')
def movie():
    datalist = []
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = "select * from movie250"
    data  = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template("movie.html",datalist=datalist)
def home():
    return index()

@app.route('/score')
def score():
    scorelist = []
    countscorelist = []
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scorelist.append(item[0])
        countscorelist.append(item[1])
    cur.close()
    conn.close()
    return render_template("score.html",scorelist=scorelist,countscorelist=countscorelist)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
