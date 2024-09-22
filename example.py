from kissbill import *

bills_file = get_bills('bills.toml')
parsed_bills = parse_bills(bills_file)
emergency_fund = Fund(total_bills(parsed_bills))

print(f' You can save (per month): {total_can_save(parsed_bills)}')
print(f' You need to save (for a six month emergency fund): {total_need_saved(parsed_bills, [emergency_fund])}')
print(f' You can make an emergency fund in {emergency_fund_savings(parsed_bills, [emergency_fund])} months.')
