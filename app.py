from flask import Flask, request, jsonify
from models import db, MyData
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def verify_token(token):
    return token == app.config['APP_SECRET']

@app.route('/upload', methods=['POST'])
def upload_data():
    token = request.headers.get('Authorization')
    if not token or not verify_token(token):
        return jsonify({"message": "Unauthorized"}), 401

    if request.is_json:
        data = request.get_json()
        try:
            objects = [MyData(**item) for item in data]
            db.session.bulk_save_objects(objects)
            db.session.commit()
            return jsonify({"message": "Data inserted successfully"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "An error occurred", "error": str(e)}), 500
    else:
        return jsonify({"message": "Request body must be JSON"}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

