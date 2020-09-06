from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit')
def submission_page():
    return render_template('submit.html')


@app.route('/addUser')
def add_user():
    return render_template('addUser.html')


@app.route('/reports')
def reports():
    return render_template('reports.html')


if __name__ == "__main__":
    app.run(debug=True)
