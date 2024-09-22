from kissbill import *

bills_file = get_bills('bills.toml')
parsed_bills = parse_bills(bills_file)
print(total_bills(parsed_bills)*6)
emergency_fund = Fund(total_bills(parsed_bills)*6)

print(total_can_save(parsed_bills))
print(total_need_saved(parsed_bills, [emergency_fund]))
