from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # This is where you handle the form data after user submits the form
        username = request.form.get('username')  # example form field
        email = request.form.get('email')
        password = request.form.get('password')

        # Add your logic here (e.g., save user to database)
        print(f"Received signup: {username}, {email}")

        # After processing, redirect or render a success page
        return redirect(url_for('home'))

    # For GET requests just show the signup form
    return render_template('signup.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
