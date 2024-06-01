from app import db
import uuid
class Customers(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.String, primary_key=True, unique=True, default=lambda: str(uuid.uuid4()))
    company_id = db.Column(db.String, db.ForeignKey('company.id'))
    name = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    website = db.Column(db.String)
    state = db.Column(db.String)
    city = db.Column(db.String)
    zipcode = db.Column(db.String)
    customer_type = db.Column(db.String)  # Adjust data type if necessary
    subType = db.Column(db.String)  # Adjust data type if necessary
    status = db.Column(db.String)  # Adjust data type if necessary
    subStatus = db.Column(db.String)  # Adjust data type if necessary
    leadSource = db.Column(db.String)  # Adjust data type if necessary
    leadStatus = db.Column(db.String)  # Adjust data type if necessary
    pipelineStatus = db.Column(db.String)  # Adjust data type if necessary
    pipelineSubStatus = db.Column(db.String)  # Adjust data type if necessary
    title = db.Column(db.String)
    bpStatus = db.Column(db.String)  # Adjust data type if necessary
    relationshipToCustomer = db.Column(db.String)
    primaryAssignment = db.Column(db.String)
    secondaryAssignment = db.Column(db.JSON)
    subscriptionStatus = db.Column(db.String)  # Adjust data type if necessary
    customFieldDropDown = db.Column(db.String)
    customFieldPrice = db.Column(db.Float)
    customFieldDates = db.Column(db.DateTime)
    nextFollowUpDate = db.Column(db.DateTime)
    customFields = db.Column(db.JSON)
    notes = db.Column(db.JSON)
    fed_id = db.Column(db.String)
    w9_form = db.Column(db.String)
    irs = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    processed_actions = db.relationship('processed_actions', backref='customers', lazy=True)
    sessions = db.relationship('Sessions', backref='customers', lazy=True)
