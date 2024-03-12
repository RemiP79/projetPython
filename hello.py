from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template

#from flask import request
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()



app = Flask(__name__)

@app.route("/")

def accueil():
    return render_template('accueil.html')
   
#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"


@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s profile'

with app.test_request_context():
    print(url_for('accueil'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


