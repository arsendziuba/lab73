class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_date_valid(day, month, year):
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
        return False

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        if cls.is_date_valid(day, month, year):
            return cls(day, month, year)
        else:
            print("Invalid date string.")
            return None

    @staticmethod
    def from_string_static(date_str):
        day, month, year = map(int, date_str.split('-'))
        if Date.is_date_valid(day, month, year):
            return Date(day, month, year)
        else:
            print("Invalid date string.")
            return None

# Creating Date objects using classmethod and staticmethod
date1 = Date.from_string("12-04-2022")
date2 = Date.from_string_static("30-02-2023")

# Checking the instances
if isinstance(date1, Date):
    print(f"Valid date: {date1.day}-{date1.month}-{date1.year}")
else:
    print("Invalid date.")

if isinstance(date2, Date):
    print(f"Valid date: {date2.day}-{date2.month}-{date2.year}")
else:
    print("Invalid date.")
