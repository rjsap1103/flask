# jinja2 - 파이썬에서 만든걸 웹에서 보여주는 용도
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
# 여기까지 절대 불변

def home():
  conn = mysql.connector.connect(host= 'localhost', user='root', password='11111', database='library_db')
  cursor = conn.cursor()
  cursor.execute('select * from books')
  books = cursor.fetchall()
  conn.close()

  return render_template('index.html', books=books)

if __name__ == '__main__':
  app.run(debug=True)


