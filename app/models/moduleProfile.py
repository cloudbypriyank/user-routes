from app import db

class ModuleProfile(db.Model):
    __tablename__ = 'module_profile'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    profile_name = db.Column(db.String(255))
    kb = db.Column(db.Boolean, default=False)
    call = db.Column(db.Boolean, default=False)
    assistants = db.Column(db.Boolean, default=False)
    chat_with_documents = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    base_plan = db.relationship("BasePlan", backref=db.backref("module_profile", lazy=True))
