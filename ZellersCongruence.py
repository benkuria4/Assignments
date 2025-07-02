from datetime import datetime

class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.original_month = month
        self.day = day

        # Adjust months: March = 3, ..., January = 13, February = 14
        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

        self.K = self.year % 100  # Year within century
        self.J = self.year // 100  # Century

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        # Zeller's Congruence formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Zeller's output: 0=Saturday, 1=Sunday, ..., 6=Friday
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

while True:
    while True:
        try:
            # Get user input
            day = int(input("\nEnter day: "))
            month = int(input("Enter month: "))
            year = int(input("Enter year: "))

            datetime(year, month, day)  # Raises ValueError if invalid
            break
        except ValueError:
            print("Invalid date. Please enter a valid day, month, and year.")

    date = DateCalculator(year, month, day)
    result = date.calculate_day_of_week()
    print(f"The day of the week for {day:02d}/{month:02d}/{year} is: {result}")

    # Ask if the user wants to try again
    repeat = input("\nDo you want to check another date? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Goodbye!")
        break
