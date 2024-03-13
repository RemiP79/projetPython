from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = 'database.db'
    # Existing code omitted

    from . import db
    db.init_app(app)

    return app
