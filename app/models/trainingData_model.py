from app import db
from .enums.enums import LLMSEnum

class TrainingData(db.Model):
    __table_name__ = "training_data"
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    company_id =db.Column(db.String(36), db.ForeignKey('company.id'), nullable=False)
    fags = db.Column(db.JSON)
    model = db.Column(db.Enum(LLMSEnum,name='LLMSEnum'))
    trained_data = db.Column(db.JSON)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
