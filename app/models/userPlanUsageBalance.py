from app import db

class UserPlanUsageBalance(db.Model):
    __tablename__ = 'user_plan_usage_balance'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    no_of_emails_per_month = db.Column(db.Integer)
    no_of_calls_per_month = db.Column(db.Integer)
    no_of_emails_per_day = db.Column(db.Integer)
    no_of_calls_per_day = db.Column(db.Integer)
    plan_id = db.Column(db.String, db.ForeignKey('company_plan.id'), nullable=False)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())