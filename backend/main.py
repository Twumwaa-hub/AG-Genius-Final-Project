from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        print(f"Received signup: {username}, {email}")

        return redirect(url_for('home'))

    # Render signup.html template on GET
    return render_template('signup.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
