from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str

class Appointment(BaseModel):
    id: int
    patient_id: int
    provider_id: int
    date_time: datetime
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    sender_id: int
    recipient_id: int
    content: str

class Message(BaseModel):
    id: int
    sender_id: int
    recipient_id: int
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True

class MedicalRecordCreate(BaseModel):
    patient_id: int
    document: str

class MedicalRecord(BaseModel):
    id: int
    patient_id: int
    document: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PrescriptionCreate(BaseModel):
    patient_id: int
    medication: str
    dosage: str
    instructions: str

class Prescription(BaseModel):
    id: int
    patient_id: int
    medication: str
    dosage: str
    instructions: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class BillingRecordCreate(BaseModel):
    patient_id: int
    service: str
    amount: int
    insurance_claim_status: str

class BillingRecord(BaseModel):
    id: int
    patient_id: int
    service: str
    amount: int
    insurance_claim_status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
