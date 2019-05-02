from flask_api import FlaskAPI, status, exceptions
from flask import request, url_for
from scrapt import scrapt
from models import models

app = FlaskAPI(__name__)


# begin news
@app.route('/news')
def news_list():
    data = models.viewnews()
    return data


@app.route('/refresh_news')
def news_refresh():
    data = models.viewnews()
    return data


@app.route('/detail_news/<int:id>')
def detail_news(ids):
    data = models.detailnews(ids)
    return data


# end news

# begin user
@app.route('/user')
def user():
    return


if __name__ == '__main__':
    app.run()
