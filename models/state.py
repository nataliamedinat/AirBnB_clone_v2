#!/usr/bin/python3
"""
This module contains one class, State
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """State has a name and relationship to cities objs
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete,delete-orphan"),
        passive_deletes=True,
        single_parent=True)

    @property
    def cities(self):
        """return a dict of City instances with state_id"""
        return {k: v for k, v in storage.all().items()
                if v.state_id == self.id}
