from app import db
from .enums.enums import AssistantTypeEnum, LLMSEnum
class ApiKeys(db.Model):
    __tablename__ = 'api_keys'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    api_type = db.Column(db.Enum(LLMSEnum,name='LLMSEnum'))
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    customer_key = db.Column(db.String)
    api_key = db.Column(db.String)
    description = db.Column(db.String)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    assistant = db.relationship('Assistants', backref='api_keys', uselist=False)