from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '13 Jan, 1997'
    },
    {
        'author': 'Angel Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '20 May, 1999'
    }
]

@app.route("/")
def hello():
    return render_template('Home page.html')
    return "<h1>Home Page!!</h1>"

@app.route("/About")
def about():
    return "<h1> About page </h1>"


#if __name__ == '__main__':
#    app.run(debug = True)