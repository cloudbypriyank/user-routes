from app import db
class UserMetaData(db.Model):
    __tablename__ = 'user_meta_data'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    ip_address = db.Column(db.String)
    login_time = db.Column(db.DateTime)
    logout_time = db.Column(db.DateTime)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    requests = db.relationship('Requests', backref=db.backref('user_meta_data', lazy=True))
