# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, redirect, url_for, render_template,request
#from markupsafe import escape
from flask import g

DATABASE = 'database.db'

def get_db():
    """Retrieve a connection to DATABASE"""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def close_connection(exception):
    """Close connection to DATABASE"""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
        """Initializes DATABASE by executing script contained in a file schema.sql"""    
        with app.app_context():
            db = get_db()
            db.cursor().execute("PRAGMA encoding = 'UTF-8';")  # Configue UTF-8

            with app.open_resource('schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()


app = Flask(__name__)

@app.route("/")
def welcome():
    """Database initialization upon home page connection"""
    if 'db' not in g:
        init_db()
    else :
        get_db()
    return render_template('welcome.html')

@app.route("/login", methods=['GET','POST'])
def auth():
    """Handles user authentication - retrieves the email and password from the login form"""
    if request.method == 'POST':          
        email = request.form['email']
        password = request.form['password']
        db = get_db()
        cursor = db.execute(f"SELECT * FROM user WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()
        close_connection(None)
        # Credentials validation
        if user:
            # redirect to the profile page
            return redirect(url_for('profile', username=user['username']))
        else:
            # error message
            return render_template('login.html', error="Nom d'utilisateur ou mot de passe incorrect.")
    else:        
        return render_template('login.html')

@app.route('/user/<username>',endpoint='profile')
def profile(username): 
    """Connected page - page to begin game
    Parameters: username (str)"""          
    return render_template('user.html', username=username)

@app.route('/<username>/enigme/<int:id_enigma>/', methods=['GET'])
def enigma(username, id_enigma):
    """Handles the display of an enigma page;
    Parameters: username (str) and id_enigma (int).
    Tables : enigma and bad_response"""   
       
    db = get_db()
    cursor = db.execute(f"SELECT * FROM enigma WHERE id = ?", (id_enigma,))
    enigma_info = cursor.fetchone()    
    cursor = db.execute(f"SELECT * FROM bad_response WHERE enigma_id = ?", (id_enigma,))    
    bad_responses = cursor.fetchone()
    close_connection(None)

    if enigma_info:
        image_url = enigma_info['image_url']
        title = str(enigma_info['title']).encode('iso-8859-1').decode("utf-8") 
        good_response = str(enigma_info['good_response']).encode('iso-8859-1').decode("utf-8") 
        link_good_response = str(enigma_info['link_good_response']).encode('iso-8859-1').decode("utf-8") 
        bad_response = str(bad_responses['bad_responses']).encode('iso-8859-1').decode("utf-8")     

        # Pass the enigma information to the HTML template
        return render_template('enigma.html',
                               error="Mauvaise réponse", 
                               username=username, 
                               id_enigma=id_enigma, 
                               enigma_info=enigma_info, 
                               image_url=image_url, title=title,  
                               bad_response=bad_response, 
                               good_response= good_response, 
                               link_good_response=link_good_response)
    else:
        # enigma not found    
        return "Énigme non trouvée"

@app.route('/<username>/endpage')
def endpage(username):
    """When user win"""
    return render_template("endpage.html", username=username)

with app.test_request_context():
    """Test URL generation for welcome view"""
    print(url_for('welcome'))
    
if __name__ == "__main__":
    """creates an instance of the Flask application 
    and runs the development server with debug mode enabled."""
    app.run(debug=True)

