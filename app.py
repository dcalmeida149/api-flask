import base64
from datetime import datetime
from flask import Flask, request, jsonify
from models import db, MyData, MyLog
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def verify_token(token):
    return token == app.config['APP_SECRET']
def create_my_data(item):
    allowed_columns = {'field1', 'field2'}
    return MyData(**{key: item[key] for key in item if key in allowed_columns})

@app.route('/upload', methods=['POST'])
def upload_data():
    token = request.headers.get('Authorization')
    user = request.headers.get('X-User')
    if not token or not verify_token(token) or not user:
        return jsonify({"message": "Unauthorized"}), 401

    try:
        user = base64.b64decode(user).decode('utf-8')
    except Exception as e:
        return jsonify({"message": "Error decoding user", "error": str(e)}), 400

    if request.is_json:
        data = request.get_json()
        try:
            objects = [create_my_data(item) for item in data]
            db.session.bulk_save_objects(objects)
            db.session.commit()
            # log
            log = MyLog(user=user, table_name='my_data', action='insert', timestamp=datetime.now())
            db.session.add(log)
            db.session.commit()
            return jsonify({"message": "Data inserted successfully", "user": user}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "An error occurred", "error": str(e)}), 500
    else:
        return jsonify({"message": "Request body must be JSON"}), 400

# Example curl command to test this endpoint:
# curl -X POST http://localhost:5000/upload -H "Content-Type: application/json" -H "Authorization: <token>" -H "X-User: <base64 encoded user>" -d @data.json

# JSON model that should be sent:
# [
#     {"field1": "value1_1", "field2": "value2_1"},
#     {"field1": "value1_2", "field2": "value2_2"}
# ]
# necessary headers:
# - Authorization: <token>
# - Content-Type: application/json
# - X-User: <base64 encoded user>

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

