from app import db

class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True)
    slug = db.Column(db.String(255))
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    user_role = db.relationship("RolePermissionMap", backref=db.backref("user_role"))
    user = db.relationship("User", backref=db.backref("user_role"))
