from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
#where the data based is stored
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'
db = SQLAlchemy(app)
#nullable means it iis requirdni.e title is required and same applies others 
class BlogPost(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text , nullable=False)
    author = db.Column(db.String(20),nullable=False, default='Noauthor')
    date_posted = db.Column(db.DataTime,nullable=False,default=datetime.utcnow)
#this function going to print
    def __repr__(self):
        return 'Blog post' + str(self.id)

# @app.route('/home/<string:name>')
# def hello(name):
#      return "hello , "  + name

# @app.route('/home/<int:idval>')
# def hello(idval):
#      return "hello , "  +  str(idval)

# methods=["GET","POST"]

# @app.route('/home/<string:name>/post/<int:idval>')
# def hello(name,idval):
#      return "hello , "  + name +",your id is " + str(idval)

#to send data from here to html by making lists of dictionaries
all_post = [
        {
        'title':'post 1',
        'content':'this is the content of Post1',
        'author':'ravindra'

        },
    {
        'title':'post 2',
        'content' : 'this is the content of Post2'


    }
]

@app.route('/home')
def index():
    return render_template('index.html')



@app.route('/posts')
def posts():
    return render_template('posts.html',posts = all_post)
if __name__ == "__main__":
    app.run(debug=True)



