from flask import Flask,request,redirect,render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html",menu='Admin or customer')

# Admin
@app.route('/login_admin',methods=["GET","POST"])
def login_admin():
    error = ''
    if request.method == "POST":
        if request.form['name'] == "admin" and request.form["password"] == "admin":
            return redirect("/admin_home")
        else:
            error = "Invalid name or password"
    return render_template("login_admin.html",menu='Admin Login',error = error)
            
@app.route('/admin_home',methods=["GET"])
def admin_home():
    if request.method == "GET":
        return render_template("home-admin.html",menu="Admin Home")

@app.route('/requested-appointments',methods=["GET","POST"])
def requested_appointments():
    if request.method == "GET":
        return render_template('appointments_requested.html',menu="Customer Requests")

@app.route('/accepted-appointments',methods=["GET","POST"])
def accepted_appointments():
    if request.method == "GET":
        return render_template("appointments_accepted.html",menu='Admin Accepted')

@app.route('/previous-appointments',methods=["GET","POST"])
def previous_appointments():
    if request.method == "GET":
        return render_template("past_appointments.html",menu='Past Appointments')
    
@app.route('/view_more')
def view_more():
    if request.method == "GET":
        return render_template("view_more.html",menu="Customer Details")
    
@app.route('/view_details',methods=["GET"])
def view_details():
    if request.method == "GET":
        return render_template("view_details.html",menu="Collection")

# Customer
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

time = []
sno = []
@app.route('/services_requested')
def appointments_requested():
    global time
    global sno
    return render_template("services_requested.html",menu='Requested Services',times = time,snos = sno,size=len(time))

@app.route('/customer_filling',methods=["GET","POST"])
def customer_filling():
    if request.method == "POST":
        global time
        global sno
        time.append(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        if sno:
            sno.append(sno[-1]+1)
        else:
            sno.append(1)
        return redirect("/appointment_requesting")
    elif request.method == "GET":
        return render_template("customer_filling.html",menu="Customer Filling")
