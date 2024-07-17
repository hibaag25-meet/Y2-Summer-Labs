from flask import Flask, render_template
import random


fortunes = [
    "A thrilling adventure awaits you in the near future.",
    "Your creativity will lead you to great success.",
    "An unexpected opportunity will bring you happiness.",
    "Patience is the key to unlocking your dreams.",
    "Your kindness will be repaid tenfold.",
    "A new friendship will enrich your life.",
    "Trust your instincts; they will guide you wisely.",
    "A financial windfall is headed your way.",
    "Embrace change; it will lead to personal growth.",
    "Love is just around the corner; keep your heart open."
]


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

# Route for /fortune
@app.route('/fortune')
def fortune():
    # Choose a random fortune
    random_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=random_fortune)


if __name__ == '__main__':
    app.run(debug=True, port=2000)
    # Importing random module





