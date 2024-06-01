from app import db
from .enums.enums import EmailStatusEnum

class sent_email(db.Model):
    __tablename__ = "sent_email"
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False, default=db.func.uuid_generate_v4())
    email_template_id = db.Column(db.String(36), db.ForeignKey('email_templates.id'))
    plan_id = db.Column(db.String, db.ForeignKey('company_plan.id'), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(EmailStatusEnum,name='EmailStatusEnum'), nullable=False)
    sent_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
