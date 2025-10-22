def check_loan_eligibility(balance):
    if balance > 50000000:
        return "✅ واجد شرایط دریافت وام هستید."
    else:
        return "❌ متاسفانه شرایط لازم را ندارید."

# تست
miyangin = float(input("میانگین موجودی 6 ماه اخیر خود را وارد کنید: "))
print(check_loan_eligibility(miyangin))
