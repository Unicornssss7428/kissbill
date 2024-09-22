import toml
class MoneyEvent:
    def __init__(self, due, amount, e_type):
        self.due = due
        self.amount = amount
        self.e_type = e_type

class Fund:
    def __init__(self, balance):
        self.balance = balance

def get_bills(file):
      with open(file) as f:
          toml_bills = toml.load(f)
          return toml_bills
  
def parse_bills(bills_dict):
      bills: list[MoneyEvent] = []
      for item in bills_dict:
          if "Payday" not in item:
              payday = MoneyEvent(int(bills_dict[item]['due']), int(bills_dict[item]['amount']), "bill")
              bills.append(payday)
          else:
              bill = MoneyEvent(int(bills_dict[item]['due']), int( bills_dict[item]['amount']), "payday")
              bills.append(bill)
      return bills

# Calculate total bills for day/week/month.
def total_bills(parsed_bills, start, end):
    total_bills = 0
    for event in parsed_bills:
        if "Payday" not in event and event.due >= start and event.due <= end:
            total_bills += event.amount
    return total_bills

# Calculate total pay for day/week/month
def total_pay(parsed_bills, start, end):
    total_pay = 0
    for event in parsed_bills:
        if "Payday" in event and event.due >= start and event.due <= end:
            total_pay += 0
# How much can I spend each day/week/month and still pay for expenses/save for emergency fund, car, etc.
def total_spending_power(parsed_bills, funds, option):
    pass

# Calculate how much I need to save per day/week/month to pay for expenes and reach funds goals.
def total_need_saved(parsed_bills, funds, option):
    pass

# Calculate how much a certain financial decision on a certain date (due) effects ability to pay for expenses and save for funds.
def if_spend(parsed_bills, funds, due):
    pass

# Display a "calendar" that tells me how much money I can spend on each day of the month while still being able to pay for my expenses and funds.
def calendar(parsed_bills, funds):
    pass
