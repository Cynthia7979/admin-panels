import random
import string
from flask import Flask, render_template, redirect, url_for, abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AE5963C9BECD7B8514FAD7996C39E'

passphrase_of_today = ''.join(
    random.SystemRandom().choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=8)
)


class LoginForm(FlaskForm):
    user_name = StringField('Username')
    password = PasswordField('Password')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = LoginForm()
    msg = ''
    if form.is_submitted():
        name, password = form.user_name.data, form.password.data
        print(name, password)
        if name == 'GhWor103' and password == 'GmDv%9dKY]':
            return redirect(url_for('admin_home', passphrase=passphrase_of_today))
        elif name and password:
            msg = 'Invalid Username or Password'
        else:
            msg = ''
    return render_template('index.html', form=form, msg=msg)


@app.route('/admin_home/?<passphrase>')
@app.route('/admin_home')
def admin_home(passphrase=''):
    if passphrase != passphrase_of_today:
        abort(401)
    else:
        return render_template('admin_home.html', passphrase=passphrase)


@app.route('/database/?<passphrase>')
@app.route('/database')
def database(passphrase=''):
    if passphrase != passphrase_of_today:
        abort(401)
    else:
        return render_template('database.html', passphrase=passphrase)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(401)
def invalid_credential(e):
    return render_template('401.html'), 401
