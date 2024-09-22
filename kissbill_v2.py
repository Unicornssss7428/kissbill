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

