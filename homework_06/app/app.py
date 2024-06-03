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
from forms import UserForm, PostForm

app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI='postgresql+pg8000://user:example@pg:5432/blog',
                  SECRET_KEY='development key',
                  SQLALCHEMY_ECHO=False)

db.init_app(app)
migrate = Migrate(app, db)


@app.get('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/create_user/', methods=['GET', 'POST'])
def create_user():
    user_form = UserForm()
    if user_form.validate_on_submit():
        db.session.add(User(username=user_form.username.data,
                            email=user_form.email.data,
                            name=user_form.name.data))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_user.html', form=user_form)


@app.route('/create_post/<user>/', methods=['GET', 'POST'])
def create_post(user):
    post_form = PostForm()
    if post_form.validate_on_submit():
        user_id = User.query.filter_by(name=user).first().id
        db.session.add(Post(author=user,
                            title=post_form.title.data,
                            body=post_form.body.data,
                            user_id=user_id,
                            ))
        db.session.commit()
        return redirect(url_for('view_posts',user=user))
    return render_template('create_post.html',user=user, form=post_form)



@app.get('/view_post/')
@app.get('/view_post/<user>/')
def view_posts(user=None):
    if user is None:
        posts = Post.query.all()
    else:
        posts = Post.query.filter_by(author=user).all()
    return render_template('views_post.html', posts=posts)





if __name__ == "__main__":
    app.run(debug=True)
