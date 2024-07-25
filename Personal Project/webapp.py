from flask import Flask, render_template, request, redirect, url_for
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
        user = auth.create_user_with_email_and_password(email, password)
        
        ref = db.child('users').child(user['localId'])
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
            user = auth.sign_in_with_email_and_password(email, password)
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

    UID = ref['user']['localId']
    user = db.child("Users").child(UID).get().val()
    return render_template("display_user.html", email=user["email"])

    email = request.args.get('email')
    username = request.args.get('username')
    location = request.args.get('location')
    travel_dates = request.args.get('travel_dates')
    locations = request.args.get('locations')

    return render_template('summary.html', 
                           email=user["email"], 
                           username=user["username"], 
                           location=user["location"], 
                           travel_dates=user["travel_dates"], 
                           locations=user["locations"]
@app.route('/options')
@app.route('/options')
def options():
    return render_template('options.html')

if __name__ == '__main__':
    app.run(debug=True, port=50011)
