from flask import Flask, redirect, url_for, render_template,request
from markupsafe import escape
from flaskr import db


def create_app():
    app = Flask(__name__)

    # Autres configurations de l'application...

    # Initialise la base de données
    db.init_app(app)

    # Autres configurations de l'application...

    return app


#from flask import request
#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#    else:
#        return show_the_login_form()


#app = create_app()
app = Flask(__name__)

@app.route('/user/<username>',endpoint='profile')
def profile(username):           
    return render_template('user.html.jinja', username=username)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def auth():
    if request.method == 'POST':   
        username = request.form['username']
        password = request.form['password']
            
        # Validation des informations d'identification (exemple simplifié)
        if username == 'rem' and password == '12345':
            # Informations d'identification valides, rediriger vers la page de profil
            return redirect(url_for('profile', username=username))
        else:
            # Informations d'identification incorrectes, afficher un message d'erreur ou rediriger vers la page de connexion avec un message d'erreur
            return render_template('login.html', error="Nom d'utilisateur ou mot de passe incorrect.")
    else:
        # Afficher le formulaire de connexion  
        return render_template('login.html')




@app.route('/<username>/enigme/<int:id_enigme>')
def enigme(username, id_enigme):
    return render_template('enigme.html.jinja', username=username, id_enigme=id_enigme)



with app.test_request_context():
    print(url_for('welcome'))


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"


#@app.route('/login')
#def login():
#    return 'login'
