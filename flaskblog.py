from flask import Flask , render_template, url_for, flash, redirect
from forms import  RegistrationFrom,LoginForm

#instantiate flask variable , __name__ is similar to main
app = Flask(__name__)

app.config['SECRET_KEY']= '779fd751a43373c448714eaa1669fb7a'

posts =[
    {'author':'Anand CR',
     'title':'Post1',
     'date':'April 20'
     },
    {'author':'Aravind CR',
     'title':'Post 2',
     'date':'April 20'}
]


#this decorator will handlethe backend
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form =RegistrationFrom()
    if form.validate_on_submit():
        # success is a bootstrap class
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Register',form=form)


if __name__ == '__main__':
    app.run(debug=True)