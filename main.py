balance = 5000


print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")
print("4. Exit")

choices = input("Pick numbers ( 1 - 3 ): ")

def check_balance():
  return f"Current Balance {balance}"

def withdraw(amount):
  global balance
  if amount <= 0:
    return "Invalid Amount. Please Try Again"
  elif amount > balance:
    return "Insufficient Funds."
  else:
    balance -= amount
    return f"Withdrawal Sucsessful. New Balance {balance}"
    
def deposit(amount):
  global balance
  if amount <= 0:
    return "Invalid Amount. Please Try Again"
  else:
   balance += amount
  return f"Deposit Sucsessful. New Balance {balance}"
  

if choices == "1":
  print(check_balance())
  
elif choices == "2":
  amount = float(input("Enter Amount to Withdraw: "))
  print(withdraw(amount))
elif choices == "3":
  amount = float(input("Enter Amount to Deposit: "))
  print(deposit(amount))
elif choices == "4":
  print("Thank you for using.")
else:
  print("Invalid Choices. Please Try Again!")
