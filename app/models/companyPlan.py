from app import db
from sqlalchemy import Column, String, ARRAY
import uuid
class CompanyPlan(db.Model):
    __tablename__ = 'company_plan'

    id = db.Column(db.String, primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    plan_type = db.Column(db.String)
    llms = db.Column(ARRAY(String))
    is_active = db.Column(db.Boolean, default=True)
    visibility_profile = db.Column(db.String)  # Adjust data type if necessary
    assistant_daily_budget = db.Column(db.Float)
    assistant_monthly_budget = db.Column(db.Float)
    no_of_emails_per_month = db.Column(db.Integer)
    no_of_calls_per_month = db.Column(db.Integer)
    no_of_emails_per_day = db.Column(db.Integer)
    no_of_calls_per_day = db.Column(db.Integer)
    max_allowed_token = db.Column(db.Integer)
    max_number_of_kb = db.Column(db.Integer)
    max_number_of_action = db.Column(db.Integer)
    max_no_assistants = db.Column(db.Integer)
    plan_expiry_date = db.Column(db.DateTime)
    assistants_daily_budget = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    base_plan_id = db.Column(db.String, db.ForeignKey('base_plan.id'))
    notes = db.Column(db.JSON)
    knowledge_base = db.relationship('KnowledgeBase',backref='company_plan', lazy=True)
    assistants = db.relationship('Assistants', backref='company_plan', lazy=True)
    processed_actions = db.relationship('processed_actions', backref='company_plan', lazy=True)
    invoice = db.relationship('Invoice', backref='company_plan', lazy=True)
    sessions = db.relationship('Sessions', backref='company_plan', lazy=True)
    user_plan_usage_balance = db.relationship('UserPlanUsageBalance', backref='company_plan', lazy=True)
    sent_email = db.relationship('sent_email', backref='company_plan', lazy=True)
