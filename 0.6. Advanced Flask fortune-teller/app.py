from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
    return render_template('home.html')

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
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

    index = len(birth_month) % len(fortunes)
    user_fortune = fortunes[index]
    return f"Your fortune: {user_fortune}"

if __name__ == '__main__':
    app.run(debug=True , port=5002)
