from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_folder='static/static')

# Configure SQLAlchemy for MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:IamawesomE1#@localhost/chemistry'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Define Chemical model
class Chemical(db.Model):
    __tablename__ = 'Chemicals'
    chemical_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    formula = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(50))

# Route to render the index.html page with chemicals
@app.route('/')
def index():
    chemicals = Chemical.query.all()
    return render_template('index.html', chemicals=chemicals)

# Route to add chemicals (POST method)
@app.route('/add-chemical', methods=['POST'])
def add_chemical():
    chemical1_name = request.form.get('chemical1')
    chemical2_name = request.form.get('chemical2')
    response = f"Added chemicals: {chemical1_name}, {chemical2_name}"
    return jsonify({'message': response})

# Route to trigger reaction (POST method)
@app.route('/trigger-reaction', methods=['POST'])
def trigger_reaction():
    response = "Simulated chemical reaction..."
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
