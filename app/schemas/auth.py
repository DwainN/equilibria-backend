"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# ============ AUTH SCHEMAS ============
class UserRegister(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    is_admin: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ RECOVERY SCHEMAS ============
class RecoveryInput(BaseModel):
    """Manual recovery data input from user"""
    sleep_hours: Optional[float] = Field(None, ge=0, le=24)
    sleep_quality: Optional[int] = Field(None, ge=1, le=10)
    soreness_level: Optional[int] = Field(None, ge=1, le=10)
    energy_level: Optional[int] = Field(None, ge=1, le=10)
    stress_level: Optional[int] = Field(None, ge=1, le=10)


class RecoveryResponse(BaseModel):
    id: int
    user_id: int
    date: datetime
    sleep_hours: Optional[float]
    sleep_quality: Optional[int]
    soreness_level: Optional[int]
    energy_level: Optional[int]
    stress_level: Optional[int]
    recovery_score: Optional[float]
    recommended_intensity: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ WEARABLE SCHEMAS ============
class WearableDataInput(BaseModel):
    """Input from wearable devices"""
    source: str = Field(..., description="apple_health, google_fit, polar_h10, etc.")
    measurement_date: datetime
    
    # HRV
    hrv_rmssd: Optional[float] = None
    hrv_sdnn: Optional[float] = None
    
    # Heart Rate
    resting_heart_rate: Optional[int] = None
    avg_heart_rate: Optional[int] = None
    
    # Sleep
    sleep_duration_minutes: Optional[int] = None
    deep_sleep_minutes: Optional[int] = None
    rem_sleep_minutes: Optional[int] = None
    
    # Activity
    steps: Optional[int] = None
    active_calories: Optional[int] = None
    
    raw_data: Optional[dict] = None


class WearableDataResponse(BaseModel):
    id: int
    user_id: int
    source: str
    sync_timestamp: datetime
    hrv_rmssd: Optional[float]
    hrv_sdnn: Optional[float]
    resting_heart_rate: Optional[int]
    avg_heart_rate: Optional[int]
    sleep_duration_minutes: Optional[int]
    deep_sleep_minutes: Optional[int]
    rem_sleep_minutes: Optional[int]
    steps: Optional[int]
    active_calories: Optional[int]
    measurement_date: datetime
    
    class Config:
        from_attributes = True


# ============ WORKOUT SCHEMAS ============
class WorkoutCreate(BaseModel):
    name: str
    description: Optional[str] = None
    workout_type: Optional[str] = None
    is_template: bool = False
    exercises: list


class WorkoutResponse(BaseModel):
    id: int
    user_id: int
    name: str
    description: Optional[str]
    workout_type: Optional[str]
    is_template: bool
    exercises: list
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True


class WorkoutSessionCreate(BaseModel):
    workout_id: Optional[int] = None
    duration_minutes: Optional[int] = None
    exercises_completed: list
    notes: Optional[str] = None


class WorkoutSessionResponse(BaseModel):
    id: int
    user_id: int
    workout_id: Optional[int]
    session_date: datetime
    duration_minutes: Optional[int]
    exercises_completed: list
    total_volume: Optional[float]
    notes: Optional[str]
    
    class Config:
        from_attributes = True