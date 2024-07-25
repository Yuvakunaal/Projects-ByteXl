from flask import Flask,request,redirect,render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("actors.html",menu='Admin or customer')

@app.route('/login_admin',methods=["GET","POST"])
def login_admin():
    if request.method == "GET":
        return render_template("login_admin.html",menu='Admin Login')
    elif request.method == "POST":
        return redirect("/")

@app.route('/login_customer',methods=["GET","POST"])
def login_customer():
    if request.method == "GET":
        return render_template("login_customer.html",menu='Customer Login')
    elif request.method == "POST":
        return redirect("/customer_home")


@app.route('/signup_customer',methods=["GET","POST"])
def signup_customer():
    if request.method == "GET":
        return render_template("signup.html",menu="Customer register")
    elif request.method == "POST":
        return redirect("/login_customer")
    
@app.route('/customer_home',methods=["GET"])
def customer_home():
    if request.method == "GET":
        return render_template("home.html",menu="Customer Home")

@app.route('/services')
def services():
    return render_template("services.html",menu='Services')

@app.route('/appointment_requesting')
def appointment_requesting():
    return render_template("appointment_requesting.html",menu="Requesting Appointment")

@app.route('/appointments_requested')
def appointments_requested():
    return render_template("appointments_requested.html",menu='Requested Appointment')
