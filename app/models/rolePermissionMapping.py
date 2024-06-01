from app import db
import uuid
class RolePermissionMap(db.Model):
    __tablename__ = 'role_permission_map'

    id = db.Column(db.String(255), primary_key=True, unique=True,default=lambda: str(uuid.uuid4()))
    role_id = db.Column(db.Integer, db.ForeignKey('user_role.id'), nullable=False)
    permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)