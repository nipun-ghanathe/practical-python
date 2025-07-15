# sears.py

bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
days = 1

while num_bills * bill_thickness < sears_height:
    print(days, num_bills, num_bills * bill_thickness)
    days = days + 1
    num_bills = num_bills * 2

print("\nNumber of days", days)
print("Number of bills", num_bills)
print("Final height", num_bills * bill_thickness)
