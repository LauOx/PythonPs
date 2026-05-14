#!/bin/usr/evn python3

from __future__ import annotations
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class Name(BaseModel):
    """Check and validate station data"""
    contact_id: str = Field(..., min_length=5, max_length=15)
    #completar

    @model_validator(mode='after')
    def validate_(self) -> Name:
        if self.x > self.y:
            raise ValidationError("blabla")
        return self

