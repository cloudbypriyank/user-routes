from app import db

class KnowledgeBase(db.Model):
    __tablename__ = 'knowledge_base'

    id = db.Column(db.String(255), primary_key=True, unique=True)
    name = db.Column(db.String(255))
    company_id = db.Column(db.String(255), db.ForeignKey('company.id'))
    user_plan_id = db.Column(db.String(255), db.ForeignKey('company_plan.id'))
    status = db.Column(db.Boolean)
    files = db.Column(db.JSON)
    urls = db.Column(db.JSON)
    faqs = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    assistants = db.relationship("Assistants", back_populates="knowledge_base")
