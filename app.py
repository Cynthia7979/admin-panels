import random
import string
from flask import Flask, render_template, redirect, url_for, abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = open('key').read()

passphrase_of_today = ''.join(
    random.SystemRandom().choices(string.ascii_uppercase+string.ascii_lowercase+string.digits, k=8)
)

Bootstrap(app)


class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = LoginForm()
    if form.validate_on_submit():
        name, password = form.user_name.data, form.password.data
        if name == 'GhWor103' and password == 'GmDv%9dKY]':
            return redirect(url_for('admin', passphrase=passphrase_of_today))
    return render_template('index.html', form=form)


@app.route('/admin/?psp=<passphrase>')
def admin(passphrase):
    if passphrase != passphrase_of_today:
        abort(401)
    else:
        return '<p>TODO(</p>'
