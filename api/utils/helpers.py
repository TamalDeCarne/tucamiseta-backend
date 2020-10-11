from flask import jsonify
from api import db


class Examiner(object):
    __slots__ = ['id', 'model', 'schema', 'unwanted_columns', 'json_data']
    def __init__(self, id=None, model=None, schema=None, unwanted_columns=None,
                 json_data=None):
        self.id = id
        self.model = model
        self.schema = schema
        self.unwanted_columns = unwanted_columns
        self.json_data = json_data


def get_rows(model, schema):
    return jsonify([schema.dump(m) for m in model.query.all()])


def insert_row(examiner):
    missing_fields, examiner.json_data = verify_fields_and_json_data( examiner.json_data, examiner.model, examiner.unwanted_columns)
    if len(missing_fields) == 0:
        new_model = examiner.model(**examiner.json_data)
        db.session.add(new_model)
        db.session.commit()
        new_model = examiner.model.query.order_by(
            examiner.model.id.desc()
        ).first()
        return examiner.schema.dump(new_model)
    else:
        return jsonify({'missing fields': missing_fields}), 400


def verify_fields_and_json_data(json_data, model, unwanted_columns):
    table_columns = [
        column.name
        for column in frozenset(model.__table__.columns)
        if column.name not in unwanted_columns
    ]
    new_json_data = {
        key: val
        for key, val in json_data.items()
        if key in table_columns
    }
    for field in frozenset(new_json_data):
        if field in table_columns:
            table_columns.remove(field)
    
    return table_columns, new_json_data
