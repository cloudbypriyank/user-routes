from app import db

class Sessions(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    assistant_id = db.Column(db.Integer, db.ForeignKey('assistants.id'))
    from_ = db.Column(db.String(255))  # Renamed from 'from' to avoid keyword conflict
    to = db.Column(db.String(255))
    session_type = db.Column(db.String(255))
    direction = db.Column(db.String(255))
    medium = db.Column(db.String(255))
    customer_id = db.Column(db.String(255), db.ForeignKey('customers.id'))
    plan_id = db.Column(db.String, db.ForeignKey('company_plan.id'))
    session_started_at = db.Column(db.DateTime)
    session_ended_at = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    session_cost = db.Column(db.Float)
    session_state = db.Column(db.String(255))
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    processed_actions = db.relationship('processed_actions', backref='sessions', lazy=True)
