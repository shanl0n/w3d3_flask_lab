import datetime

from models.event import Event

event1 = Event("Mob programming", datetime.date(2023, 7, 19), 14, "The classroom", "we're gonna try and mob this lab!!", False)

event2 = Event("Glastonbury", datetime.date(2023, 6, 10), 10000, "The South", "Madness, Music, Mugs", True)

event3 = Event("E3", datetime.date(2023, 9, 30), 8000, "LA", "Games expo", False)

events = [event1, event2, event3]




