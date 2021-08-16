print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?\n"))
if tip!='10'or '12' or '15':
  print("Please Enter a correct digit")
else:
  split=int(input("How many people to split the bill?\n"))
  tip_percent=tip/100
  totalBill = bill+ tip_percent
  bill_per_person=totalBill / split
  finalAmount= round(bill_per_person, 2)
  print(f"Each person will pay : ${finalAmount}")
