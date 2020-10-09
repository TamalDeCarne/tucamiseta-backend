from api.models import City
from api import ma


class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
    id = ma.auto_field()
    estado_id = ma.auto_field()
    clave = ma.auto_field()
    nombre = ma.auto_field()
