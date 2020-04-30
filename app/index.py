from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/trainers')
def trainers():
    return render_template('trainers.html')

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')


@app.route('/user/<name>') #ostanek 
def user(name):
    return render_template('user.html', name=name)