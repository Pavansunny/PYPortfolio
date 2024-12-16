from flask import Flask, render_template

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    return render_template('index.html')

# Projects Route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
