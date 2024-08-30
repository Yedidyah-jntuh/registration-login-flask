from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

# Local variable to store user credentials and information
users = {}

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        dob = request.form['dob']
        gender = request.form['gender']
        hobbies = request.form['hobbies'].split(',')

        # Trim whitespace around each hobby
        hobbies = [hobby.strip() for hobby in hobbies]

        # Check if passwords match
        if password != confirm_password:
            return "Passwords do not match. Please try again."

        # Store user data
        users[username] = {
            'password': password,
            'email': email,
            'dob': dob,
            'gender': gender,
            'hobbies': hobbies
        }

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for('profile'))

        return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/profile')
def profile():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    user = users[username]
    return render_template('profile.html', username=username, user=user)

if __name__ == '__main__':
    app.run(debug=True)
git remote set-url origin git@github.com:Yedidyah-jntuh/registration-login-flask.git
