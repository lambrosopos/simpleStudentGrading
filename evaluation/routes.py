from flask import request, render_template, redirect, flash, url_for
from evaluation import app, db
from evaluation.models import User, Score, Subject
from evaluation.forms import ScoreForm, UserForm


@app.route('/', methods=['POST', 'GET'])
def reports():
    if request.method == 'POST':
        user_id = request.form
        return user_id
    else:
        users = User.query.order_by(User.date_created).all()
        return render_template('reports.html', users=users)


@app.route('/submit', methods=['POST', 'GET'])
def submission_page():
    if request.method == 'POST':
        form = request.form
        return form
    else:
        users = User.query.order_by(User.date_created).all()
        return render_template('submit.html', users=users)


@app.route('/addUser', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!', 'success')

            user = request.form
            new_user = User(username=user['username'], email=user['email'])

            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            except:
                return 'Unable to add user'

    return render_template('addUser.html', form=form)

