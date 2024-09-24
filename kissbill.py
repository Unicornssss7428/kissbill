import toml
class MoneyEvent:
    def __init__(self, due, amount, e_type):
        self.due = due
        self.amount = amount
        self.e_type = e_type
# Balance is for 1 month, duration is the amount of months.
# i.e. for an emergency fund I need 1759 a month, my emergency fund should last me 6 months so I need 1759*6 cash in the fund.
class Fund:
    def __init__(self, balance, duration=6):
        self.duration = duration
        self.balance = balance*6

# Displays a balance for each day.
class MoneyCalendar:
    pass

def total_funds(funds):
    total_funds = 0
    for fund in funds:
        total_funds += fund.balance
    return total_funds
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
def total_bills(parsed_bills, start=1, end=31):
    total_bills = 0
    for event in parsed_bills:
        if event.e_type != 'payday' and event.due >= start and event.due <= end:
            total_bills += event.amount
    return total_bills

# Calculate total pay for day/week/month
def total_pay(parsed_bills, start=1, end=31):
    total_pay = 0
    for event in parsed_bills:
        if event.e_type == 'payday' and event.due >= start and event.due <= end:
            total_pay += event.amount 
    return total_pay

# Calculate how much I need to save per day/week/month to pay for expenses and reach funds goals.
def total_need_saved(parsed_bills, funds, option='m'):
   bills_total = total_bills(parsed_bills) 
   funds_total = total_funds(funds)
   total_expenses = bills_total + funds_total
    
   # Total expenses 
   return total_expenses

def total_can_save(parsed_bills):
    bills_total = total_bills(parsed_bills)
    pay_total = total_pay(parsed_bills)
    return pay_total - bills_total
        
# Calculate how much a certain financial decision on a certain date (due) effects ability to pay for expenses and save for funds.
def if_spend(parsed_bills, funds, due):
    pass


def emergency_fund_savings(parsed_bills, funds):
    need_total_saved = total_need_saved(parsed_bills, funds)
    can_total_save = total_can_save(parsed_bills)

    return need_total_saved / can_total_save

# Display a "calendar" that tells me how much money I can spend on each day of the month while still being able to pay for my expenses and funds.
def calendar(parsed_bills, funds):
    pass

