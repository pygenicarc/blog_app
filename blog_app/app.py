from flask import Flask, render_template
# from utils.db import db

flask_app = Flask(__name__)



@flask_app.route('/')
def index():
    return render_template('index.html')


@flask_app.route('/about')
def about():
    return render_template('about.html')


@flask_app.route('/blogs')
def blogs():
    blogs_list = [
        {
            "blog_id":1,
            "blog_title":"blog one",
            "blog_content":"blog dummy content",
            "author":"Author 1",
            "date":"28/11/2024"
         },
        {
            "blog_id": 2,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 3,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 4,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 5,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 6,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
    ]
    return render_template('blogs.html', blogs=blogs_list)


@flask_app.route('/add-blog')
def add_blog():
    return render_template('add_blog.html')


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )