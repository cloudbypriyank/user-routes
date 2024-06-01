from app import db
from .enums.enums import DepartmentEnum,UserStatusEnum
import uuid
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone = db.Column(db.String)
    status = db.Column(db.Enum(UserStatusEnum,name='UserStatusEnum'))
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'))
    notes = db.Column(db.JSON)
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    department = db.Column(db.Enum(DepartmentEnum,name='UserStatusEnum'))
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    created_by = db.Column(db.String)
    updated_by = db.Column(db.String)
    user_meta_data = db.relationship('UserMetaData', backref=db.backref('user', lazy=True))
    note = db.relationship('Note', backref=db.backref('user', lazy=True))