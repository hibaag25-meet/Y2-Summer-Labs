from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    if 'name' not in session or 'birth_month' not in session:
        return redirect(url_for('login'))
    
    name = session['name']
    return render_template('home.html', name=name)

@app.route('/fortune')
def fortune():
    if 'birth_month' not in session:
        return redirect(url_for('login'))
    
    fortunes = [
        "You will have a great day!",
        "Something unexpected will happen.",
        "You will achieve your goals.",
        "A surprise is waiting for you.",
        "You will make a new friend.",
        "You will find what you are looking for.",
        "An old friend will reappear in your life.",
        "You will discover a new hobby.",
        "A financial opportunity is coming your way.",
        "You will enjoy good health."
    ]

    birth_month = session['birth_month']
    index = len(birth_month) % len(fortunes)
    user_fortune = fortunes[index]
    session['fortune'] = user_fortune
    return render_template('fortune.html', fortune=user_fortune)

if __name__ == '__main__':
    app.run(debug=True, port=5006)
