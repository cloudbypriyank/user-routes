from app import db
import uuid
from .enums.enums import ProcessedActionTypeEnum
import uuid
class Actions(db.Model):
    __tablename__ = 'actions'

    id = db.Column(db.String, primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    name = db.Column(db.String(56))
    type = db.Column(db.Enum(ProcessedActionTypeEnum,name='ProcessedActionTypeEnum'))
    email = db.Column(db.String(50))
    sms = db.Column(db.String)
    webhook = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    processed_actions = db.relationship('processed_actions', backref=db.backref('actions', lazy=True))
