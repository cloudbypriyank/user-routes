from app import db
from .enums.enums import ConversationTypeEnum
import uuid


class conversations(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.String(255), primary_key=True, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    call_id = db.Column(db.String(255), unique=True)
    conversation_uuid = db.Column(db.String(255))
    conversation_type = db.Column(db.Enum(ConversationTypeEnum,name='ConversationTypeEnum'))
    input_text = db.Column(db.Text)
    input_tokens = db.Column(db.Text)
    no_of_input_tokens = db.Column(db.Integer)
    output_tokens = db.Column(db.Text)
    no_of_output_tokens = db.Column(db.Integer)
    price = db.Column(db.Float)
    session_id = db.Column(db.String, db.ForeignKey('sessions.id'))
    text = db.Column(db.String(255))
    notes = db.Column(db.JSON)
    v_response = db.Column(db.JSON)
    ai_thread_id = db.Column(db.String(255))
    ai_message_ids = db.Column(db.String(255))
    processed_action_id = db.Column(db.String(255))
    parameters = db.Column(db.JSON)
    intents = db.Column(db.JSON)
    entities = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    processed_actions = db.relationship('processed_actions', backref=db.backref('conversations', lazy=True))

