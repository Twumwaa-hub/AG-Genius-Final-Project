from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Your frontend homepage

@app.route('/signup')
def signup():
    return render_template('signup.html')  # Your signup page

# Add other routes as needed

if __name__ == "__main__":
    app.run(debug=True)
