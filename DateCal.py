class DateCal:
    def __init__(self, year: int, month: int, day: int):
        """
        Initialize the DateCal class with year, month, and day.

        Parameters:
            year (int): The year in YYYY format.
            month (int): The month (1-12).
            day (int): The day of the month (1-31).
        """
        self.year = year
        self.month = month
        self.day = day

    def adjust(self):
        """
        Adjust the month and year if the month is January or February.
        """
        if self.month == 1 or self.month == 2:
            self.month += 12  # Treat January as 13th and February as 14th month
            self.year -= 1  # Adjust the year to the previous year

        # Calculate K (year of the century) and J (zero-based century)
        self.K = self.year % 100
        self.J = self.year // 100

    def calculate_weekday(self):
        """
        Calculate the day of the week using Zeller's Congruence formula.


        """
        # Apply Zeller's Congruence formula
        h = (self.day + ((13 * (self.month + 1)) // 5) + self.K + (self.K // 4) + (self.J // 4) + (5 * self.J)) % 7


        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days_of_week[h]

    def display_result(self):
        """
        Display the result of the weekday calculation.
        """
        self.adjust()  # Adjust the month/year before calculating
        weekday = self.calculate_weekday()
        print(f"The day of the week for {self.month}/{self.day}/{self.year} is {weekday}.")


# Example usage
if __name__ == "__main__":
    # Create an instance of DateCal for February 2, 2006
    calculator = DateCal(2006, 2, 2)

    # Display the result
    calculator.display_result()
