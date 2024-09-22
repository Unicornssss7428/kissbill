from kissbill_v2 import *

bills_file = get_bills('bills.toml')
parsed_bills = parse_bills(bills_file)
print(total_pay(parsed_bills))
