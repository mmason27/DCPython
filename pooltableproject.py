import datetime

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None
        self.end_time = None
        self.is_occupied = False
     
    def checkout(self): 
        self.is_occupied = True
        self.start_time = datetime.datetime.now()

    def checkin(self):
        self.is_occupied = False
        self.end_time = datetime.datetime.now()

    def total_time(self):
        self.total_time = self.end_time - self.start_time
        return self.total_time

    def time_played(self):
        return datetime.datetime.now() - self.start_time

