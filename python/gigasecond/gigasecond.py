from datetime import date, timedelta
import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime

def add(moment):
    """
    Given a moment, determine the moment that would be after a gigasecond has passed.
    A gigasecond is 10^9 (1,000,000,000) seconds.
    """

    t1=datetime.seconds(10**9)
    return t1+timedelta(moment)