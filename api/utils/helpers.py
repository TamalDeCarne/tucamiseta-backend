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
