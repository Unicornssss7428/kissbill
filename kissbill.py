import toml
import sys

class MoneyEvent:
    def __init__(self, due: int, amount:int, e_type:str ):
        self.due = due
        self.e_type = e_type
        self.amount = amount

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

def total_bills(parsed_bills):
    total_bills = 0
    for event in parsed_bills:
        if event.e_type == "bill":
            total_bills += event.amount
    return total_bills    

def bill_calendar(parsed_bills, start_money, starting_from = 0):
    # Bills.toml should be sorted.
    money = int(start_money)
    for event in parsed_bills:
        if event.e_type == "bill" and event.due >= int(starting_from):
           print(f"On {event.due} you have: {money - event.amount}")
           money -= event.amount 
        elif event.e_type == "payday" and event.due >= int(starting_from):
            print(f"On {event.due} you have: {money + event.amount}")
            money+= event.amount
    return money

# Determines if I go in the red when spending a certain amount of money.
def if_i_spend(parsed_bills,  spending):
    bills_total = total_bills(parsed_bills)
    if int(spending) > bills_total:
        print(f"You'll be left with { bills_total - int(spending)} at the end of the month, idiot.")
    return bills_total - int(spending)

def calc_net(current_cash, debt):
    return current_cash - debt


# Determines how much money you need for an emergency fund in x months.
def emergency_fund(parsed_bills, months):
    bills_total = total_bills(parsed_bills)*months
    return int(bills_total / months)

#How much money can you save for an emergency fund, outputs how long to save.
def save_for_emergency_fun(parsed_bills,  can_save, months=6):
    emergency_total = emergency_fund(parsed_bills, months)*months
    print(emergency_total)
    print(int(emergency_total/can_save))

def monthly_pay(parsed_bills):
    pay = 0
    for event in parsed_bills:
        if event.e_type == 'payday':
            pay+=event.due
    return pay


# Determines how much money I can save per day.
# Determines how much money I can save per month.
# Determines how much money I can save per year.
def determine_savings(parsed_bills, amount_time):
    pass     

