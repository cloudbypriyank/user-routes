from flask import jsonify

def success_response(message, fc=False):
    if fc:
        return jsonify(status=True, **message), 200
    return jsonify(status=True, data=message), 200

def created_response(message):
    return jsonify(status=True, data=message), 201

def error_response(message):
    return jsonify(status=False, error=message), 400

def unauthorized_response(message):
    return jsonify(status=False, error=message), 401

def internal_error_response(message):
    return jsonify(status=False, error=message), 500