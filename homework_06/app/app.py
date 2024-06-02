from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for)

from flask_migrate import Migrate
from flask_sqlalchemy.session import Session
from sqlalchemy import select

from models import db
from models import User
from models import Post
from forms import UserForm,PostForm

app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI='postgresql+pg8000://user:example@localhost:5432/blog',
                  SECRET_KEY='development key',
                  SQLALCHEMY_ECHO=True)

db.init_app(app)
migrate = Migrate(app, db)


@app.get('/')
def index():
    stmt = (select(User.name,User.email, User.username))
    users = db.session.scalars(stmt)
    return render_template('index.html', users=users)


@app.route('/add/', methods=['GET', 'POST'])
def create_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        db.session.add(User(username=user_form.username.data,
                             email=user_form.email.data,
                             name=user_form.name.data))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_user.html', form=user_form)

@app.get('/view_post/')
@app.get('/view_post/<user>/')
def view_posts(user=None):
    if user is None:
        posts = Post.query.all()
    else:
        posts = Post.query.join(User).join(User.id).filter(User.name == user).all()
    return render_template('views_post.html', posts=posts, user=user)

@app.route('/add/', methods=['GET', 'POST'])
def create_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        db.session.add(Post(title=post_form.title.data,
                            body=post_form.body.data,
                            author=post_form.author.data,
                            ))
        db.session.commit()
        return redirect(url_for('views_post.html'))
    return render_template('create_post.html', form=post_form)

if __name__ == "__main__":
    app.run(debug=True)
