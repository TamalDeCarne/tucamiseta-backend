from api import db

class City(db.Model):
    __tablename__ = "municipios"
    id = db.Column(db.Integer, primary_key=True)
    estado_id = db.Column(db.Integer)
    clave = db.Column(db.String(3))
    nombre = db.Column(db.String(100))


class State(db.Model):
    __tablename__ = "estados"
    id = db.Column(db.Integer, primary_key=True)
    clave = db.Column(db.String(2))
    nombre = db.Column(db.String(40))
    abrev = db.Column(db.String(10))
    activo = db.Column(db.SmallInteger)


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    city_id = db.Column(db.Integer, nullable=True)
    state_id = db.Column(db.Integer, nullable=True)
    message_type = db.Column(db.Enum('Pregunta', 'Cotizacion'))
    body = db.Column(db.Text)
    date_recieved = db.Column(db.String(100))