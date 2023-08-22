from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gas_meters.db'
db = SQLAlchemy(app)

class GasMeter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    date_measured = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')

#DODAVANJE PLINOMJERA
@app.route('/add_meter', methods=['POST'])
def add_meter():
    data = request.json
    meter = GasMeter(owner=data['owner'], street=data['street'], city=data['city'], state=data['state'])
    db.session.add(meter)
    db.session.commit()
    return jsonify({"message": "Plinomjer dodan uspijesno!"}), 201

#BRISANJE PLINOMJERA
@app.route('/delete_meter/<int:id>', methods=['DELETE'])
def delete_meter(id):
    meter = GasMeter.query.get(id)
    if meter:
        db.session.delete(meter)
        db.session.commit()
        return jsonify({"message": "Plinomjer izbrisan uspijesno!"}), 200
    return jsonify({"message": "Ne postoji ID!"}), 404

#FILTER PLINOMJERA PO DATUMU MJERENJA ILI GRADU 
@app.route('/filter', methods=['GET'])
def filter_meters():
    date = request.args.get('date')
    city = request.args.get('city')
    
    query = GasMeter.query
    
    if date:
        query = query.filter(GasMeter.date_measured == datetime.strptime(date, '%Y-%m-%d'))
    if city:
        query = query.filter(GasMeter.city == city)
    
    meters = query.all()
    result = [{"id": meter.id, "owner": meter.owner, "street": meter.street, "city": meter.city, "state": meter.state, "date_measured": meter.date_measured.strftime('%Y-%m-%d')} for meter in meters]
    return jsonify(result)


#UREDIT STANJE PLINOMJERA 
@app.route('/edit_meter/<int:id>', methods=['PUT'])
def edit_meter(id):
    data = request.json
    meter = GasMeter.query.get(id)
    if meter:
        meter.owner = data['owner']
        meter.street = data['street']
        meter.city = data['city']
        meter.state = data['state']
        db.session.commit()
        return jsonify({"message": "Plinomjer uređen uspješno!"}), 200
    return jsonify({"message": "Ne postoji ID!"}), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

