from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_time(timezone):
    """ return the current time in the given timezone"""
    timezone = ZoneInfo(timezone)
    return datetime.now(timezone).strftime("%H:%M:%S")