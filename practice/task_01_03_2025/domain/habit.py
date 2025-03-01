import time
import datetime
import random
import string


class Habit:
    def __init__(self, title: str, description: str, period: int):
        self.habit_id = self.generate_id()
        self.title = title
        self.description = description
        self.period = period
        self.start_date = int(time.time())
        self.is_completed = False

    @staticmethod
    def generate_id(length=16):
        timestamp = str(int(time.time() * 1000000))
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(timestamp)))
        return timestamp + random_chars

    def check_status(self):
        now = int(time.time())
        days_since_start = (now - self.start_date) // self.period
        next_due = self.start_date + (days_since_start + 1) * self.period
        return datetime.datetime.fromtimestamp(next_due).strftime("%Y-%m-%d %H:%M:%S")
