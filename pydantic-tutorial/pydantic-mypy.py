# coding: utf8
# ===================================
# Author: yumingmin
# File: pydantic-mypy.py
# Cate: FastAPI
# Create time: 2022/7/12 14:17
# Update time: 
# ===================================
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, NoneStr


class Model(BaseModel):
    age: int
    first_name = 'John'
    last_name: NoneStr = None
    signup_ts: Optional[datetime] = None
    list_of_ints: List[int]


m = Model(age=42, list_of_ints=[1, '2', b'3'])
print(m.age)  # not a model field!
Model()