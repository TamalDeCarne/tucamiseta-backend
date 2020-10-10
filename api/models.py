from api import db


class City(db.Model):
    __tablename__ = "municipios"
    id = db.Column(db.Integer, primary_key=True)
    estado_id = db.Column(db.Integer)
    clave = db.Column(db.String(3))
    nombre = db.Column(db.String(100))
