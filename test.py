from kissbill import *

bills_file = get_bills('bills.toml')
parsed_bills = parse_bills(bills_file)
print(total_bills(parsed_bills))
