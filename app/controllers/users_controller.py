from http import HTTPStatus
from flask import Blueprint, request, jsonify
from app.services.user_service import (
    create_user, get_user_by_id, delete_user, update_user, insert_user,
    insert_customer, get_company_by_email, get_user_by_email, insert_company,
    send_email, signup_email_template, create_session
)
from app.utils.responsesUtils import (
    error_response, internal_error_response, unauthorized_response,
    success_response, created_response
)
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from datetime import timedelta

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user_route():
    data = request.get_json()
    name = data.get('name')  # Change to 'name'
    email = data.get('email')
    user = create_user(name, email)
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_bp.route('/users/<string:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), HTTPStatus.OK
    else:
     return jsonify({"message": "User not found"}), 404

@user_bp.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/users/<string:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    user = update_user(user_id, name, email)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200
    return jsonify({"message": "User not found"}), 404

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    phone = data.get('phone')
    address = data.get('address')
    password = data.get('password')
    company = data.get('company')

    if not firstname or not lastname or not email:
        return error_response("Mandatory fields are missing")

    if get_user_by_email(email):
        return error_response("User already exists with the same email")

    company_id = insert_company({
        'company_name': company.get('company_name'),
        'customer_name': company.get('customer_name'),
        'industry': company.get('industry')
    })

    user_data = {
        'name': f"{firstname} {lastname}",
        'email': email,
        'phone': phone,
        'password': password,
        'company_id': company_id,
    }
    user_id = insert_user(user_data)

    if user_id:
        customer_data = {
            'name': f"{firstname} {lastname}",
            'email': email,
            'address': address,
            'phone': phone,
            'state': None,
            'city': None,
            'zipcode': None,
            'company_id': company_id
        }
        insert_customer(customer_data)
        
        send_email(email, "Welcome to Contact Swing – Start Communicating Smarter!", signup_email_template(user_data['name']))
        return created_response(user_data)

    return error_response("Failed to create a User.")

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return error_response('Invalid request!')

    user = get_user_by_email(email)

    if not user or not check_password_hash(user.password_hash, password):
        return error_response('Invalid credentials!')

    session_id = create_session(user.id, request.remote_addr)
    if not session_id:
        return error_response('Failed to create session!')

    additional_claims = {
        'email': user.email,
        'username': user.name,
        'session_id': session_id,
        'user_id': user.id,
        'role': user.role,
        'company_id': user.company_id,
    }

    access_token = create_access_token(
        identity=additional_claims,
        expires_delta=timedelta(seconds=current_app.config['TOKEN_VALIDITY'])
    )

    return success_response({
        'user_id': user.id,
        'message': 'Authenticated successfully',
        'access_token': access_token
    })
