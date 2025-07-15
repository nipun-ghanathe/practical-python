# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

month = 0
while principal > 0:
    month += 1
    month_payment = (
        payment + extra_payment
        if extra_payment_start_month <= month <= extra_payment_end_month
        else payment
    )

    amount = principal * (1 + rate / 12)
    month_payment = min(month_payment, amount)
    principal = principal * (1 + rate / 12) - month_payment
    total_paid = total_paid + month_payment

    print(month, round(total_paid, 2), round(principal, 2))

print("\nTotal paid", round(total_paid, 2))
print("Months paid", month)
