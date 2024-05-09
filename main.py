import datetime



class DebtTracker:
    def __init__(self):
        self.debts = {}
        self.interest_rates = {}

    def add_debt(self, name, amount):
        if name in self.debts:
            self.debts[name] += amount
        else:
            self.debts[name] = amount

    def set_interest_rate(self, name, weekday_rate, weekend_rate=None):
        if weekend_rate is None:
            weekend_rate = weekday_rate
        self.interest_rates[name] = (weekday_rate, weekend_rate)

    def calculate_interest(self, name):
        if name not in self.interest_rates:
            print(f"No interest rate found for {name}")
            return
    interest_rate = self.get_interest_rate(name)
    if name in self.debts:
        self.debts[name] += self.debts[name] * interest_rate

    def get_interest_rate(self, name):
        today = datetime.datetime.now()
        weekday_rate, weekend_rate = self.interest_rates[name]
        if today.weekday() in [5, 6]:  # Saturday or Sunday
            return weekend_rate
        else:
            return weekday_rate

    def user_input(self, name):
        name = input("Enter the name: ")
        amount = float(input("Enter the current money owed: "))
        rate_type = input("Do you want to enter the interest rate in cents per day or percentage per day? (cents/percentage): ")
        if rate_type.lower() == 'cents':
            weekday_rate = float(input("Enter the weekday interest rate (in cents per day): ")) / amount
            weekend_rate_choice = input("Do you want to set a different interest rate for weekends? (yes/no): ")
            if weekend_rate_choice.lower() == 'yes':
                weekend_rate = float(input("Enter the weekend interest rate (in cents per day): ")) / amount
            else:
                weekend_rate = weekday_rate
        else:
            weekday_rate = float(input("Enter the weekday interest rate (in percentage per day): ")) / 100
            weekend_rate_choice = input("Do you want to set a different interest rate for weekends? (yes/no): ")
            if weekend_rate_choice.lower() == 'yes':
                weekend_rate = float(input("Enter the weekend interest rate (in percentage per day): ")) / 100
            else:
                weekend_rate = weekday_rate
        self.add_debt(name, amount)
        self.set_interest_rate(name, weekday_rate, weekend_rate)

# Example usage
tracker = DebtTracker()
tracker.user_input()
tracker.calculate_interest(name)
print(tracker.debts)
