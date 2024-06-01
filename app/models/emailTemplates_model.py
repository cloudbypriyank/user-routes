from app import db

class EmailTemplates(db.Model):
    __tablename__ = 'email_templates'
    id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False, default=db.func.uuid_generate_v4())
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    name = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    sent_emails = db.relationship('sent_email', backref=db.backref('email_templates', lazy=True))
