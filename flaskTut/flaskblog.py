from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='83hgwdy2873hdw5723871g1y4817usg1'

postLists = [
	{
	  'author' 		: 'Saikat Mondal',
	  'title'  		: 'Blog Post 1',
	  'content'		: 'First post content goes here',
	  'date_posted' : 'Aug 17, 2018'
	},
	{
	  'author' 		: 'Macoda Mondal',
	  'title'  		: 'Blog Post 2',
	  'content'		: 'Second post content goes here',
	  'date_posted' : 'Aug 18, 2018'
	}
]

@app.route("/")
@app.route("/Home")
def home():
    return render_template('home.html',posts=postLists)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])    
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created!!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/Login",methods=['GET','POST'])    
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data== 'admin@blog.com' and form.password.data== 'password':
			flash('you have been logged in!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessfull.Please check username and password','danger')	
	return render_template('login.html',title='Login',form=form)		
	
if __name__ == '__main__':
	app.run(debug=True)