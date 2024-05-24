"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

program_url = ['https://cdn.otus.ru/media/public/be/cf/becf7d85261a4b9db10a56f8d187c849.png',
               'https://cdn.otus.ru/media/public/87/cd/87cd08ade5884958a72a92b54fb06f73.png',
               'https://cdn.otus.ru/media/public/b3/f4/b3f4563a92be4f6fbe7be943d19ac4b5.png']

@app.route('/')
def index():
    return render_template('index.html', image_url = program_url)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)