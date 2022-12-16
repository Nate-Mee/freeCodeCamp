import math

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.balance = 0
    self.tot_withdraw = 0

  def check_funds(self, amount):
    if self.balance - amount >= 0:
      return True
    else:
      return False
 
  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
    
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      amount = -amount
      self.ledger.append({"amount": amount, "description": description})
      self.balance += amount
      self.tot_withdraw += amount
      return True
    else:
      return False
      
  def get_balance(self):
    return self.balance

  def transfer(self, amount, dest):
    withdraw_desc = f'Transfer to {dest.category}'
    deposit_desc = f'Transfer from {self.category}'
    if self.check_funds(amount):
      self.withdraw(amount, withdraw_desc)
      dest.deposit(amount, deposit_desc)
      return True
    else:
      return False

  #Printed Budget
  def __str__(self):

    # Title Line
    asterisk_calc = ((30 - len(self.category)) / 2)
    if asterisk_calc.is_integer():   
      asterisk = '*' * int(asterisk_calc)
      title_line = f"{asterisk}{self.category}{asterisk}"
    else:
      asterisk_start = '*' * int(asterisk_calc + 0.5)
      asterisk_end = '*' * int(asterisk_calc - 0.5)
      title_line = f"{asterisk_start}{self.category}{asterisk_end}" 

    # Ledger Lines
    lines = ''
    for num in range(0,len(self.ledger)):
      description = self.ledger[num]["description"]
      amount = '{:.2f}'.format(self.ledger[num]["amount"])
      while len(str(amount)) > 7:
        amount.pop()
      spaces = ' ' * (30 - len(str(amount)) - (len(description) if len(description) <= 23 else 23))
      line = f"{description[:23]}{spaces}{amount}\n"
      lines += line
    
    # Total Line
    total_line = f"Total: {'{:.2f}'.format(self.balance, 2)}"

    # Print Statement
    return f"{title_line}\n{lines}{total_line}"

#Bar Chart
def create_spend_chart(cat_list):

  # Calculations
  categories = {}
  total = 0
  for cat in cat_list:
    total += cat.tot_withdraw
    categories[cat.category] = cat.tot_withdraw

  for entry in categories:
    categories[entry] = math.floor((categories[entry] / total) * 10) * 10
# Categories dict now has category as key, and percentage of total withdrawals rounded down to nearest 10, as value.

  # Bars
  y_axis = 100
  bars = ''
  while y_axis >= 0:
    if y_axis == 100:
      bars += f"{y_axis}|"
    elif y_axis == 0:
      bars += f"  {y_axis}|"
    else:
      bars += f" {y_axis}|"
    for entry in categories:
      if y_axis <= categories[entry]:
        bars += ' o '
      else:
        bars += '   '
    bars += ' \n'
    y_axis -= 10

  # Dashes
  dashes = '    ' + ('-' * ((len(categories) * 3) + 1))

  # Bar Labels
  labels = ''
  cat_names = list(categories.keys())
  count = 0
  while count < max([len(name) for name in cat_names]):
    line = '     '
    for n in range(0, len(cat_names)):
      try:
        line += f"{cat_names[n][count]}  "
      except:
        line += '   '
    count += 1
    if count == max([len(name) for name in cat_names]):
      labels += f"{line}"
    else:
      labels += f"{line}\n"
  
  # Print Statement
  return f"Percentage spent by category\n{bars}{dashes}\n{labels}"


# food = Category('food')
# food.deposit(20, 'pay')
# food.withdraw(10, 'apples and a lot of them')
# fuel = Category('fuel')
# fuel.deposit(30, 'pay')
# food.transfer(7, fuel)
# fuel.withdraw(20, 'fill tank')
# rent = Category('rent')
# rent.deposit(100, 'pay')
# rent.withdraw(50, 'sept')
# print(food.ledger, food.balance)
# print(fuel.ledger, fuel.balance)
# print(food)
# categories_list = [food, fuel, rent]
# create_spend_chart(categories_list)

# entertainment = Category('entertainment')
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# transfer_amount = 20
# food_balance_before = food.get_balance()
# entertainment_balance_before = entertainment.get_balance()
# good_transfer = food.transfer(transfer_amount, entertainment)
# food_balance_after = food.get_balance()
# entertainment_balance_after = entertainment.get_balance()
# actual = food.ledger[2]
# expected = {"amount": -transfer_amount, "description": "Transfer to Entertainment"}
# print('Food:', food_balance_before, food_balance_after)
# print('Entertainment:', entertainment_balance_before, entertainment_balance_after)
# print(actual, '\n', expected)

# business = Category('business')
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# actual = create_spend_chart([business, food, entertainment])
# expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(expected)

