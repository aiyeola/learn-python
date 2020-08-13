has_high_income = True
has_good_credit = True
has_guarantor = False
has_criminal_record = False

if has_good_credit and has_high_income:
    print("Eligible for loan")

if has_good_credit or has_guarantor:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
