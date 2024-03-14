import sqlite3
from flask import Flask, redirect, url_for, render_template,request
#from markupsafe import escape
from flask import g

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():    
        with app.app_context():
            db = get_db()
            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()

app = Flask(__name__)

@app.route('/user/<username>',endpoint='profile')
def profile(username):           
    return render_template('user.html', username=username)

@app.route("/")
def welcome():
    if 'db' not in g:
        init_db()
    else :
        get_db()
    return render_template('welcome.html')

@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

@app.route("/login", methods=['GET','POST'])
def auth():
    if request.method == 'POST':          
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        cursor = db.execute('SELECT * FROM user WHERE email=? AND password=?', (email, password))
        user = cursor.fetchone()
        # Validation des informations d'identification
        if user:
            # Informations d'identification valides, rediriger vers la page de profil
            return redirect(url_for('profile', username=user['username']))
        else:
            # Informations d'identification incorrectes, afficher un message d'erreur ou rediriger vers la page de connexion avec un message d'erreur
            return render_template('login.html', error="Nom d'utilisateur ou mot de passe incorrect.")
    else:
        # Afficher le formulaire de connexion  
        return render_template('login.html')




@app.route('/<username>/enigme/<int:id_enigme>/', methods=['GET'])
def enigme(username, id_enigme):
    db = get_db()   
    cursor = db.execute('SELECT * FROM enigma WHERE id = ?', (id_enigme,))
    enigme_info = cursor.fetchone()  
    
    cursor = db.execute('SELECT * FROM bad_response WHERE id = ?', (id_enigme,))
    bad_responses = cursor.fetchone()

    if enigme_info:
        image_url = enigme_info['image_url']
        title = enigme_info['title']
        good_response = enigme_info['good_response']
        link_good_response = enigme_info['link_good_response']
        bad_response = bad_responses['bad_responses']

        # Passer les informations de l'énigme à la template HTML
        return render_template('enigme.html', username=username, id_enigme=id_enigme, enigme_info=enigme_info, image_url=image_url, title=title, bad_responses_info=bad_responses,  bad_response=bad_response, good_response= good_response, link_good_response=link_good_response)
    else:
        # Gérer le cas où l'énigme n'est pas trouvée
        return "Énigme non trouvée"



with app.test_request_context():
    print(url_for('welcome'))


if __name__ == "__main__":
   # app = create_app()
    app.run(debug=True)

