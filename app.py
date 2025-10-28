from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"New message from {name} ({email}): {message}")
        return "Thanks for contacting me!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
