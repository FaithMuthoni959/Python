class DateCalculator:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def set_details(self):
        months = [
            "march", "april", "may", "june", "july", "august",
            "september", "october", "november", "december",
            "january", "february"
        ]

        self.day = int(input("Enter the day: "))
        month_input = input("Enter the month (e.g. January or February): ").lower().strip()
        self.year = int(input("Enter the year: "))

        if month_input in months:
            month_index = months.index(month_input) + 3  # March = 3 ... January = 13, February = 14
            if month_index > 12:  # January (13) or February (14)
                self.year -= 1  # Adjust year for Zeller's formula
            self.month = month_index
        else:
            print("Invalid month name entered.")
            self.set_details()  # Retry input

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        Y = self.year

        K = Y % 100
        J = Y // 100

        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

calc = DateCalculator()
calc.set_details()
print(f"The day of the week is: {calc.calculate_day_of_week()}")
