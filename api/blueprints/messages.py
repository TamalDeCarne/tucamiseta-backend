from flask import Blueprint, jsonify, request
from flask_cors import CORS
from json import loads as jloads
from api.models import Message
from api.schemas import MessageSchema
from api.utils import helpers

message = Blueprint("message", __name__)
message_schema = MessageSchema()
CORS(message)

@message.route("/api/messages", methods=['GET'])
def get_messages():
    try:
        return helpers.get_rows(Message, message_schema)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@message.route("/api/message", methods=['POST'])
def new_message():
    try:
        examiner = helpers.Examiner(
            model= Message,
            schema= message_schema,
            unwanted_columns= ['id'],
            json_data= jloads(request.data)
        )
        return helpers.insert_row(examiner)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
