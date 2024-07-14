"""
This module will contain the database models for all the necessary
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Enum, LargeBinary, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import SCHEMA
from common.customTypes import UserType, NotificationType, NotificationStatus

Base = declarative_base(metadata=MetaData(schema=SCHEMA))
metadata = Base.metadata


class Vendor(Base):
    """
    Vendor here represents the company which will use our services
    """
    __tablename__ = "vendors"

    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("name", String, nullable=False)
    official_email = Column("official_email", String, nullable=False)
    address = Column("address", String, nullable=False)
    business_type = Column("business_type", String, nullable=False)
    # TODO: Get the allowed business types and make an Enum - B2B & B2C
    domain_name = Column("domain_name", String, unique=True, nullable=False)
    GSTIN = Column("GSTIN", String, unique=True, nullable=False)


class User(Base):
    """
    The common User table which will have the record for all the possible users of the system
    """
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, index=True)
    username = Column("username", String, unique=True, index=True, nullable=False)
    password = Column("password", Text, nullable=False)
    user_type = Column("user_type", Enum(UserType), nullable=False)
    is_active = Column("is_active", Boolean,  nullable=False)
    vendor_id = Column("vendor_id", Integer, ForeignKey("vendors.id"))
    users = relationship("Vendor", back_populates="vendors")


class Notification(Base):
    """
    The table to contain the metadata of the notification to be triggered
    """
    __tablename__ = "notifications"

    id = Column("id", Integer, primary_key=True, index=True)
    number_list = Column("numberList", String, nullable=False)      # TODO: update to store list
    template = Column("template", LargeBinary, nullable=False)
    type = Column("type", Enum(NotificationType), nullable=False)
    frequency = Column("frequency", Integer, default=1, nullable=False)
    user_id = Column("user_id", Integer, ForeignKey("users.id"))
    start_date_time = Column("start_date_time", DateTime, nullable=False)
    end_date_time = Column("end_date_time", DateTime, nullable=False)
    notification_status = Column(
        "notification_status", Enum(NotificationStatus), nullable=False)
    users = relationship("User", back_populates="users")


class NotificationAudit(Base):
    """
    The consideration to the Notifications, to store the inbetween status
    of the Notifications, if they are completed as expected or not.
    """
    __tablename__ = "notification_audits"
    id = Column("id", Integer, primary_key=True, index=True)
    status = Column("status", String)
    number_of_attempts = Column("number_of_attempts", Integer,
                                nullable=False, default=0)
    notification_id = Column("notification_id", Integer,
                             ForeignKey("notifications.id"))
    notifications = relationship("Notification", back_populates="notifications")
