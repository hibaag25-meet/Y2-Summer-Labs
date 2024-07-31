from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCFZ0OiQY63obxCpy4DMHz4vRb5_eR6_Bw",
    "authDomain": "triptide-9f83a.firebaseapp.com",
    "projectId": "triptide-9f83a",
    "storageBucket": "triptide-9f83a.appspot.com",
    "messagingSenderId": "774123610431",
    "appId": "1:774123610431:web:f5bf56cbf7adde1803338a", 
    "databaseURL": "https://triptide-9f83a-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        location = request.form['location']
        login_session["user"] = auth.create_user_with_email_and_password(email, password)
        
        ref = db.child('users').child(login_session["user"]['localId'])
        ref.set({
            'username': username,
            'location': location,
            'email': email

        })


        
        return redirect(url_for('options'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session["user"] = auth.sign_in_with_email_and_password(email, password)
            db.child("users").child(login_session["user"]['localId']).set({
                "username": request.form["username"],
                "email": request.form["email"],
                "location": request.form["location"]
                })
            return redirect(url_for('options'))
        except:
            return 'Authentication failed'
    return render_template('login.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/itinerary')
def itinerary():
    location = 'sample_location'
    return render_template('itinerary.html', location=location)

@app.route('/signout')
def signout():
    return redirect(url_for('home'))

@app.route('/accommodation')
def accommodation():
    return render_template('accommodation.html')
    
@app.route('/summary')
def summary():
    print(db.child("users").child(login_session["user"]["localId"]).get().val())
    return render_template("summary.html", info=db.child("users").child(login_session["user"]["localId"]).get().val())

@app.route('/options')
def options():
        return render_template('options.html')

if __name__ == '__main__':
    app.run(debug=True, port=50011)
