from flask import Flask, render_template, request, redirect, session
import pyrebase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


Config = {
  "apiKey": "AIzaSyCwP032h6f8GACQJT9OSsFTMelb22rr3LI",
  "authDomain": "authentication-lab-d7339.firebaseapp.com",
  "projectId": "authentication-lab-d7339",
  "storageBucket": "authentication-lab-d7339.appspot.com",
  "messagingSenderId": "573642124114",
  "appId": "1:573642124114:web:0e555e64e485e3f8b6688b",
  "measurementId": "G-V2Q8N1S62D" ,
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/display')
def display():
    return render_template('display.html')

if __name__ == '__main__':
    app.run(debug=True, port= 5004)


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            return redirect('/home')
        except:
            return "An error occurred. Please try again."
    return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user
            session['quotes'] = []
            return redirect('/home')
        except:
            return "An error occurred. Please try again."
    return render_template('signin.html')

@app.route('/signout')
def signout():
    session.pop('user', None)
    return redirect('/signin')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quote = request.form['quote']
        session['quotes'].append(quote)
        return redirect('/thanks')
    return render_template('home.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')
@app.route('/display')
def display():
    quotes = session.get('quotes', [])
    return render_template('display.html', quotes=quotes)

     



