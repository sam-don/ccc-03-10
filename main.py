# Loading environment variables
from dotenv import load_dotenv
load_dotenv()

# Flask application creation
from flask import Flask
app = Flask(__name__)

# Database connection
from database import init_db
db = init_db(app)

# Controller registration
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)
