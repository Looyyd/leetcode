from flask import Flask, g, request, redirect, url_for, session
import functools
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # just for example, use a secure random value in real scenarios

@app.before_request
def load_logged_in_user():
    """Before each request, check if the user is logged in by checking session."""
    user = session.get('user')
    if user is None:
        g.user = None
    else:
        g.user = user

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route('/login', methods=('GET', 'POST'))
def login():
    """Simulating login action"""
    if request.method == 'POST':
        # suppose we get username from form
        username = request.form['username']
        # in a real app, you would validate the user data here
        session.clear()
        session['user'] = username
        return redirect(url_for('secret'))

    # return a form for 'GET' request
    return '''
        <form method="POST">
            <input type="text" name="username">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/secret")
@login_required
def secret():
    return f"Hello, {g.user}! This is a secret page."

if __name__ == "__main__":
    app.run(debug=True)
