from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return 'i love imooc'

# 使用 Flask
#  pip install Flask
#  flask --version
#  export FLASK_APP=flask.py
#  flask run --host 0.0.0.0
#  127.0.0.1:5000

# Flask 为什么可以独立运行呢
## CGI
## FastCGI
## WSGI  Werkzeug
## UWSGI

