class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.quantity = 0
    self.description = ''

  def sell(self, amount):
    if self.quantity >= amount:
      self.quantity -= amount
      return True
    else:
      return False

  def stock(amount):
    self.quantity += amount
    return True
