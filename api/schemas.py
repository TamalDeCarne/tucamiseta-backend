from api.models import *
from api import ma


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
    id = ma.auto_field()
    estado_id = ma.auto_field()
    clave = ma.auto_field()
    nombre = ma.auto_field()


class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = State
    id = ma.auto_field()
    clave = ma.auto_field()
    nombre = ma.auto_field()
    abrev = ma.auto_field()
    activo = ma.auto_field()


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()
    city_id = ma.auto_field()
    state_id = ma.auto_field()
    message_type = ma.auto_field()
    body = ma.auto_field()
    date_recieved = ma.auto_field()