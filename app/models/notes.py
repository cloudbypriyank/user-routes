from app import db
class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    notes_type = db.Column(db.String)
    company_id = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    notes = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

