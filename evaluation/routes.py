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
    form = ScoreForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            score = request.form
            get_subject = Subject.query.filter_by(subject=score['subject']).first()

            if get_subject is None:
                new_subject = Subject(subject=score['subject'])

                try:
                    db.session.add(new_subject)
                    db.session.commit()
                    get_subject = Subject.query.filter_by(subject=score['subject']).first()
                except:
                    flash('Unable to add subject!', 'warning')

            else:
                new_score = Score(score=score['score'], user_id=score['user'], subject_id=get_subject.id)
                try:
                    db.session.add(new_score)
                    db.session.commit()
                    flash(f'Successfully added new score for {get_subject.subject}', 'success')
                except:
                    flash('Unable to add score!', 'danger')

    users = User.query.order_by(User.date_created).all()
    return render_template('submit.html', users=users, form=form)


@app.route('/addUser', methods=['POST', 'GET'])
def add_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():

            user = request.form
            new_user = User(username=user['username'], email=user['email'])

            try:
                db.session.add(new_user)
                db.session.commit()
                flash(f'Account created for {form.username.data}!', 'success')
                return redirect('/')
            except:
                flash('Unable to add user!', 'danger')
                return render_template('addUser.html', form=form)

    return render_template('addUser.html', form=form)

