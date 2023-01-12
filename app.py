from flask import Flask
from routes.contacts import contacts
from utils.db import db
from config import user, password, host, database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret key'
db.init_app(app)
app.register_blueprint(contacts)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(e)
if __name__ == "__main__":
    app.run(debug=True)
