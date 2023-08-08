from flask import Blueprint, render_template , url_for , request , flash , abort ,redirect
from flask_login import login_required , current_user
from models import User
from models import Workout 
from __init__ import db




main = Blueprint('main',__name__)



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html",name=current_user.name)



@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')


@main.route('/new',methods=['POST'])
@login_required
def new_workout_post():
    pushups = request.form['pushups']
    comment = request.form['comment']

    workout = Workout(pushups=pushups, comment=comment,author=current_user)
    db.session.add(workout)
    db.session.commit()

    flash("Your Workout has been added")
   
    return redirect(url_for('main.all_workouts'))

@main.route('/all')
@login_required
def all_workouts():
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(email=current_user.email).first_or_404()
    # workouts = user.workouts
    workouts = Workout.query.filter_by(author=user).paginate(page=page,per_page=3)
    return render_template('all_workouts.html',workouts=workouts,user=user)

@main.route('/delete_workout/<int:workout_id>')
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)

    # Delete the workout from the database
    db.session.delete(workout)
    db.session.commit()
    flash("Your Workout has been deleted")
    return redirect(url_for('main.all_workouts'))


@main.route('/update_workout/<int:workout_id>/update', methods=['GET', 'POST'])
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)

    if request.method == 'POST':
        workout.pushups = request.form['pushups']
        workout.comment = request.form['comment']
        flash("Your Workout has been update")

        db.session.commit()
        return redirect(url_for('main.all_workouts'))
    return render_template('update_workout.html', workout=workout)