from flask import Flask , render_template, url_for
#instantiate flask variable , __name__ is similar to main
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)