from sqlalchemy import text
from flask import Flask, jsonify
from flask_cors import CORS
import os

# Import models
from models import db, TestModel, Trip

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'planventure.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Initialize SQLAlchemy
db.init_app(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to PlanVenture API"})

@app.route('/health')
def health_check():
    try:
        # Test database connection with explicit text declaration
        db.session.execute(text('SELECT 1'))
        return jsonify({
            "status": "healthy",
            "database": "connected",
            "database_uri": app.config['SQLALCHEMY_DATABASE_URI'],
            "database_exists": os.path.exists('planventure.db')
        })
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
            "database_uri": app.config['SQLALCHEMY_DATABASE_URI'],
            "database_exists": os.path.exists('planventure.db')
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
