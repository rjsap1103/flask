# jinja2 - 파이썬에서 만든걸 웹에서 보여주는 용도
# from flask import Flask, render_template
# import mysql.connector
#
# app = Flask(__name__)
#
# @app.route('/')
# # 여기까지 절대 불변
#
# def home():
#   conn = mysql.connector.connect(host= 'localhost', user='root', password='11111', database='library_db')
#   cursor = conn.cursor()
#   cursor.execute('select name  from books')
#   books = cursor.fetchall()
#   conn.close()
#
#   return render_template('index.html', books=books)
#
# if __name__ == '__main__':
#   app.run(debug=True)

# from flask import Flask, render_template
# import mysql.connector
#
# app = Flask(__name__)
#
# def get_db_connection():
#   return mysql.connector.connect(
#     host='localhost', user='root', password='11111', database='school_db'
#   )
#
#
#
#
# @app.route('/')
# # 여기까지 절대 불변
# def show_scores():
#   conn = get_db_connection()
#   cursor = conn.cursor()
#   cursor.execute("SELECT student_id, score FROM scores")
#   scores = cursor.fetchall()
#   conn.close()
#
#   return render_template('index.html', scores=scores)
#
# if __name__ == '__main__':
#   app.run(debug=True)


# from flask import Flask, render_template, request
# import mysql.connector
#
# app = Flask(__name__)
#
# def get_db():
#   return mysql.connector.connect(
#     host='localhost', user='root', password='11111', database='movie_db'
#   )
#
# @app.route('/')
#
# def index():
#   genre = request.args.get('genre','전체')
#   conn = get_db()
#   cursor = conn.cursor()
#   if genre == '전체' :
#     cursor.execute('select title, genre, rating from movies order by rating desc')
#   else :
#     cursor.execute("select title, genre, rating from movies where genre = '%s'" % (genre,)) #<- 데이터베이스 출력은 튜플이기 때문에 튜플형식으로 만들어준다.
#
#   movies = cursor.fetchall()
#   conn.close()
#
#   return render_template('index.html',movies=movies, selected_genre=genre )
#
# if __name__ == '__main__':
#   app.run(debug=True)

# from flask import Flask, render_template
# import mysql.connector
#
# app = Flask(__name__)
#
#
# def get_db():
#   return mysql.connector.connect(
#     host='localhost', user='root', password='11111', database='cafe_db'
#   )
# @app.route('/')
# def show_sales():
#   conn = get_db()
#   cursor = conn.cursor()
#   cursor.execute("SELECT menu_name, price, quanty,(price * quanty) as total FROM sales")
#   sales = cursor.fetchall()
#   cursor.execute("select sum(price * quanty) from sales")
#   total = cursor.fetchone()[0]
#   conn.close()
#
#   return  render_template('index.html', sales=sales, total=total)
#
# if __name__ == '__main__':
#   app.run(debug=True)

from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)


def get_db():
  return mysql.connector.connect(
    host='localhost', user='root', password='11111', database='todo_db'
  )
@app.route('/')
def index():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("select id,task from todos")
  todos = cursor.fetchall()
  cursor.close()
  conn.close()
  return render_template('index.html', todos=todos)

@app.route('/add')
def add():
  task = request.args.get('task')
  if task :
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("insert into todos (task) values (%s)",(task,))
    conn.commit()
    cursor.close()
    conn.close()
  return redirect('/')


@app.route('/delete')
def delete():
  id = request.args.get('id')
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute("delete from todos where id = %s",(id,))
  conn.commit()
  cursor.close()
  conn.close()
  return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)