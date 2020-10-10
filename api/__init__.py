from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from api.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    return app


app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)


from api.blueprints.cities import city
app.register_blueprint(city)

if __name__ == "__main__":
    app.run(debug=True)
