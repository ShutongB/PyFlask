from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
posts = [
    {
        'title': 'First Post',
        'content': 'This is the first post content.',
        'author': 'John Doe'
    },
    {
        'title': 'Second Post',
        'content': 'This is the second post content.',
        'author': 'Jane Smith'
    }
]

# Home route
@app.route('/')
def home():
    return render_template('index.html', posts=posts)

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Single post route
@app.route('/post/<int:post_id>')
def post(post_id):
    if post_id < len(posts):
        return render_template('post.html', post=posts[post_id])
    else:
        return "Post not found."

# Form submission route
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        new_post = {
            'title': title,
            'content': content,
            'author': author
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    else:
        return render_template('submit.html')

if __name__ == '__main__':
    app.run()
