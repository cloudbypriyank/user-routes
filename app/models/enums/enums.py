
from enum import Enum

class EmailStatusEnum(str, Enum):
    SENT = "SENT"
    FAILED = "FAILED"
    QUEUED = "QUEUED"
    DELIVERED = "DELIVERED"
    OPENED = "OPENED"
    CLICKED = "CLICKED"

# enums/enums.py

from enum import Enum

class SubscriptionStatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    OTHER = "OTHER"

class UserStatusEnum(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    OTHER = "OTHER"

class CustomerTypeEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    B2B_CUSTOMER = "B2B_CUSTOMER"
    B2C_CUSTOMER = "B2C_CUSTOMER"
    OTHER = "OTHER"

class IndustryEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class SubIndustryEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class DepartmentEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class SubDepartmentEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class CustomerStatusEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class LeadStatusEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class SocialsEnum(str, Enum):
    X = "X"
    META = "META"
    GMAIL = "GMAIL"
    LINKEDIN = "LINKEDIN"
    SLACK = "SLACK"
    INSTAGRAM = "INSTAGRAM"
    DISCORD = "DISCORD"
    YOUTUBE = "YOUTUBE"
    OTHER = "OTHER"

class PipelineStatusEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class PlanTypeEnum(str, Enum):
    ANNUAL = "ANNUAL"
    QUARTERLY = "QUARTERLY"
    OTHER = "OTHER"

class BpStatusEnum(str, Enum):
    USER = "USER"
    COMPANY = "COMPANY"
    OTHER = "OTHER"

class VisibilityProfileEnum(str, Enum):
    HOSPITAL = "HOSPITAL"
    RESTAURANT = "RESTAURANT"
    OTHER = "OTHER"

class LLMSEnum(str, Enum):
    CHATGPT_4_0 = "CHATGPT_4_0"
    LLAMA3 = "LLAMA3"
    OTHER = "OTHER"

class AssistantTypeEnum(str, Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"
    VOICE = "VOICE"
    OTHER = "OTHER"

class SessionTypeEnum(str, Enum):
    CALL = "CALL"
    CHAT = "CHAT"
    EMAIL = "EMAIL"
    OTHER = "OTHER"

class ConversationTypeEnum(str, Enum):
    USER = "USER"
    ASSISTANT = "ASSISTANT"
    OTHER = "OTHER"

class SessionStateEnum(str, Enum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    END = "END"
    OTHER = "OTHER"

class SessionDirectionEnum(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
    OTHER = "OTHER"

class SessionMediumEnum(str, Enum):
    TWILIO = "TWILIO"
    VONAGE = "VONAGE"
    OTHER = "OTHER"

class ProcessedActionTypeEnum(str, Enum):
    EMAIL = "EMAIL"
    SMS = "SMS"
    WEBHOOK = "WEBHOOK"
    OTHER = "OTHER"

class UsageTypeEnum(str, Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"
    CALL = "CALL"
    OTHER = "OTHER"

class InvoiceStatusEnum(str, Enum):
    PAID = "PAID"
    PAYMENT_PENDING = "PAYMENT_PENDING"
    CANCELLED = "CANCELLED"
    OTHER = "OTHER"

class PaymentModeEnum(str, Enum):
    UPI = "UPI"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    OTHER = "OTHER"

class InvoiceTypeEnum(str, Enum):
    UPI = "UPI"
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"
    OTHER = "OTHER"

class RequestTypeEnum(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
