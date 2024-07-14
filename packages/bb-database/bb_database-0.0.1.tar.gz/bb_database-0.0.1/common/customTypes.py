"""
This file stores all the custom files required in the part of database
"""
from enum import Enum


class UserType(Enum):
    """
    Shows the type of system user
    """
    CUSTOMER = "Customer"
    VENDOR_ADMIN = "Vendor Admin"
    VENDOR_SPECTATOR = "Vendor Spectator"
    SUPER_ADMIN = "Super Admin"


class NotificationType(Enum):
    """
    This type will be used to show which type of notification
    is registered. Considering this type further execution way
    will be decided for the particular notification.
    """
    BROADCAST = "Broadcast"
    TRACKING_EVENT = "Tracking Event"
    RECEIPT = "Receipt"


class NotificationStatus(Enum):
    """
    Notification status to show the current sent status
    """
    CREATED = "Created"
    ACTIVE = "Active"
    COMPLETED = "Completed"
    ON_HOLD = "On Hold"
    TERMINATED = "Terminated"
