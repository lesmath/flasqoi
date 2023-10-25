from flasqoi import app
from flask import render_template, url_for, redirect, flash, request
from flasqoi.forms import RegistraionForm, LoginForm
from scamp import *



@app.route("/", methods=["GET", "POST"])
def home():
    
    melody = []
    if request.method == "POST":
        if request.form.get("play"):           
            
            pass
    return render_template("homepage.html", melody=melody)

# @app.route("/")
# def home():
#     return render_template('homepage.html', title='Home')
 
# @app.route("/home")
# def homepage():
#     return render_template('homepage.html', title='Home')

@app.route("/account")
def account():
    return render_template('account.html', title='Account')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'les@qoi.co.za' and form.password.data == '12345678':
            flash(f'Login successful for {form.email.data}!', category='success')
            return redirect(url_for('account'))
        else:
            flash(f'Login unsuccessful for {form.email.data}!', category='danger')
            return redirect(url_for('homepage'))
    return render_template('login.html', title='Login', form=form)
