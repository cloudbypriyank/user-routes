from flask import request, jsonify, current_app, _request_ctx_stack
import jwt
from functools import wraps
from datetime import datetime, timezone

def unAuthorized_response(message):
    response = jsonify({'message': message})
    response.status_code = 401
    return response

def authenticate(f):
    @wraps(f)
    def auth_function(*args, **kwargs):
        authorization = request.headers.get('Authorization',None)
        if authorization and ' ' in authorization:
            token_type, token = authorization.split(' ')
            if(token_type) != 'Bearer':
                return unAuthorized_response("Invalid Authorization type. Only bearer is accepted")
            try:
                tokenresp = jwt.decode(token,current_app.config['SECRET_KEY'], algorithms=["HS256"])
                timestamp = tokenresp.get('timestamp')
                if not timestamp:
                    return unAuthorized_response('Invalid token !')
                now = datetime.now(timezone.utc).timestamp()
                if now > timestamp + current_app.config['TOKEN_VALIDITY']:
                    return unAuthorized_response('Access token expired. Please login !')
                _request_ctx_stack.top.token = tokenresp
                return f(*args, **kwargs)
            except jwt.ExpiredSignatureError:
                return unAuthorized_response("Access token expired !")
            except jwt.InvalidTokenError:
                return unAuthorized_response("Invalid token")
        return unAuthorized_response("Invalid Authorization")
    
    return auth_function
