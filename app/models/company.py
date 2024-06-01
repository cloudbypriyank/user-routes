from app import db
import uuid
from .enums.enums import IndustryEnum,DepartmentEnum,CustomerTypeEnum
import uuid

class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.String, primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    company_name = db.Column(db.String)
    customer_name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    website = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    zip_code = db.Column(db.String)
    customer_type = db.Column(db.Enum(CustomerTypeEnum,name='CustomerTypeEnum'))  # Adjust data type if necessary
    industry = db.Column(db.Enum(IndustryEnum,name='IndustryEnum'))  # Adjust data type if necessary
    subIndustry = db.Column(db.Enum(IndustryEnum,name='IndustryEnum'))  # Adjust data type if necessary
    department = db.Column(db.Enum(DepartmentEnum,name=DepartmentEnum))  # Adjust data type if necessary
    subDepartment = db.Column(db.Enum(DepartmentEnum,name='DepartmentEnum'))  # Adjust data type if necessary
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    user_plan = db.relationship('CompanyPlan', backref='company', lazy=True)
    notes = db.Column(db.JSON)
    fields = db.Column(db.JSON)
    knowledge_base = db.relationship('KnowledgeBase', backref='company', lazy=True)
    customers = db.relationship('Customers', backref='company', lazy=True)
    api_key = db.relationship('ApiKeys', backref='company', lazy=True)
    user_roles = db.relationship('UserRole', backref='company', lazy=True)
    users = db.relationship('User', backref='company', lazy=True)
    actions = db.relationship('Actions', backref='company', lazy=True)
    training_data = db.relationship('TrainingData', backref='company', lazy=True)
    email_templates = db.relationship('EmailTemplates', backref='company', lazy=True)
