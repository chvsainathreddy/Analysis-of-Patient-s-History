
from werkzeug.wrappers import Request, Response
from history import app
from flask import render_template, redirect, url_for, flash, request, json
from history.models import Item, User, Doctor, Admin
from history.forms import DoctorLoginForm, RegisterForm, LoginForm, UpdateForm, DoctorView, AdminLoginForm, AdminUpdateForm
from history import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/history')
@login_required
def view_page():
    items = Item.query.filter_by(owner=current_user.id).order_by(Item.id.desc())
    noofrecords=len(list(items))
    return render_template('view.html', items=items, j=noofrecords, user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data,
                              name=form.name.data.capitalize(),
                              age=form.age.data,
                              gender=form.gender.data,
                              aadhar_no=form.aadhar_no.data,
                              mobileno=form.mobileno.data,
                              address=form.address.data
                              )
        db.session.add(user_to_create)
        db.session.commit()
        
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
            
        return redirect(url_for('view_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('view_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))
@app.route('/update', methods=['GET', 'POST'])
def update_page():
    form = UpdateForm()
    if form.validate_on_submit():
        user_to_update = Item(hospital_name=form.hospital_name.data,
                            doctor_name=form.doctor_name.data,
                            cause=form.cause.data,
                            city=form.city.data,
                            medicines=form.medicines.data,
                            remarks=form.remarks.data,
                            owner=current_user.id
                            )
        db.session.add(user_to_update)
        db.session.commit()
    
        flash(f'History updated successfully!', category='success')
        return redirect(url_for('view_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('update.html',form=form)

#for Doctor

@app.route('/doctor', methods=['GET', 'POST'])
def doctor_page():
    form = DoctorLoginForm()
    if form.validate_on_submit():
        attempted_user = Doctor.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password==form.password.data:
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('doctor_search_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('doctor_login.html', form=form, name = "Doctor")

@app.route('/doctorsview', methods=['GET', 'POST'])
def doctor_search_page():
    user=1
    data =[str(i) for i in User.query.all()]
    if request.method == 'POST':
        try:
            l=request.form.get('search')
            u=User.query.filter_by(username=l).first()
            items = Item.query.filter_by(owner=int(u.id)).order_by(Item.id.desc())
            noofrecords=len(list(items))
            flash(f'Medical History of a Patient : {u.name}', category='success')
            return render_template('doctorsview.html',items=items,j=noofrecords, data=data,user=u)
        except:
            flash("Enter the Name to Search!!", category='danger')
    return render_template('doctorsview.html',data=data, user=user)
#for Admin
@app.route('/admin', methods=['GET', 'POST'])
def admin_page():
    form = AdminLoginForm()
    if form.validate_on_submit():
        attempted_user = Admin.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.password==form.password.data:
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('adminview_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('admin_login.html', form=form, name = "Administrator")



@app.route('/adminview', methods=['GET', 'POST'])
def adminview_page():
    form = AdminUpdateForm()
    form.username.choices = [name for name in User.query.order_by(User.username).all()]
    if form.validate_on_submit():
        uname=form.username.data
        user=User.query.filter_by(username=uname).first()
        user_to_update = Item(hospital_name=form.hospital_name.data,
                            doctor_name=form.doctor_name.data,
                            cause=form.cause.data,
                            city=form.city.data,
                            medicines=form.medicines.data,
                            remarks=form.remarks.data,
                            owner=int(user.id)
                            )
        db.session.add(user_to_update)
        db.session.commit()
    
        flash(f'History updated successfully!', category='success')
        return redirect(url_for('adminview_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('adminview.html',form=form)
