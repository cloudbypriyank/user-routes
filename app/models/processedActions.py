from app import db
from .enums.enums import ProcessedActionTypeEnum

class processed_actions(db.Model):
    __tablename__ = 'processed_actions'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    session_id = db.Column(db.String(255), db.ForeignKey('sessions.id'))
    customer_id = db.Column(db.String(255), db.ForeignKey('customers.id'))
    action_id = db.Column(db.String(255), db.ForeignKey('actions.id'))
    plan_id = db.Column(db.String, db.ForeignKey('company_plan.id'))
    conversation_id = db.Column(db.String(255), db.ForeignKey('conversations.id'))
    message_id = db.Column(db.String(255))
    action_type = db.Column(db.Enum(ProcessedActionTypeEnum, name='processed_action_type_enum'))
    status = db.Column(db.Boolean)
    action_response = db.Column(db.JSON)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())


 



