from app.models import User, Company, Customers, Sessions
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
from flask import current_app

def create_user(username, email):
    user = User(username=username, email=email)  # Use the User class to create a new user instance
    db.session.add(user)
    db.session.commit()
    return user


def get_user_by_id(user_id):
    return User.query.get(user_id)


# delete user

def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

# update user

def update_user(user_id, name=None, email=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        db.session.commit()
        return user
    return None



# creating company data

def insert_company(data):
    company = Company(
        company_name=data.get('company_name'),
        customer_name=data.get('customer_name'),
        industry=data.get('industry'),
        
    )
    db.session.add(company)
    db.session.commit()
    return company.id


#creating users

def insert_user(data):
    user = User(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone'),
        password=generate_password_hash(data.get('password'))
    )
    db.session.add(user)
    db.session.commit()
    return user.id

#getting users

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

# getting company

def get_company_by_email(email):
    return Company.query.filter_by(email=email).first()


# craete customer

def insert_customer(data):
    customer = Customers(
        name=data.get('name'),
        email=data.get('email'),
        address=data.get('address'),
        phone=data.get('phone'),
        website=data.get('website'),
        state=data.get('state'),
        city=data.get('city'),
        zipcode=data.get('zipcode'),
        company_id=data.get('company_id'),
    )
    db.session.add(customer)
    db.session.commit()
    return customer.id


mail = Mail()

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender='team@contactswing.com'
    )
    mail.send(msg)


def signup_email_template(name):
    return f"""
    <h1>Welcome {name}!</h1>
    <p>Thank you for signing up.</p>
    """


# function for hashing

# def set_password(self,password):
#         self.password_hash = generate_password_hash(password)
    
# validating the password


def check_password(self, password):
    return check_password_hash(self.password_hash, password)


def create_session(user_id, ip_address="", source="", actions=""):
    try:
        new_session = Sessions(
            user_id=user_id,
            ip_address=ip_address,
            source=source,
            actions=actions
        )
        db.session.add(new_session)
        db.session.commit()
        return new_session.id
    except Exception as e:
        print("Error in create_session: ", e)
        return False