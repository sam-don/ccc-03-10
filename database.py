import os
from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://postgres:{os.getenv('DB_PASSWORD')}@54.91.110.61:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db
