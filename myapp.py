from flask import *
from society import addData,loginvalidation


f = Flask(__name__)

@f.route("/")
def home():
	return render_template("home.html")

@f.route("/login")
def login():	  
	return render_template("login.html")


@f.route("/reg")
def register():
	return render_template("registration.html")

@f.route("/dash")
def dashboard():
	return render_template("dashboard.html")


@f.route("/about")
def about():
	return render_template("about.html")


@f.route("/addData",methods=["POST"])
def add_Data():
	id=request.form["id"]
	fname=request.form["fname"]
	lname=request.form["lname"]
	dob=request.form["dob"]
	cont=request.form["cont"]
	email=request.form["email"]
	gender=request.form["gender"]
	uname=request.form["uname"]
	passwd=request.form["passwd"]

	t=(id,fname,lname,dob,cont,email,gender,uname,passwd)
	addData(t)
	return redirect("/login")

@f.route("/loginvalidation",methods=["POST"])
def login_validation():
	uname=request.form.get('uname')
	passwd=request.form.get('passwd')

	a=(uname,passwd)
	el=loginvalidation(a)

	if len(el)>0 :
		return render_template("dashboard.html" ,users="el")
	else:
		return render_template("login.html" ,users="el")



if __name__=="__main__":
	f.run(debug=True)
