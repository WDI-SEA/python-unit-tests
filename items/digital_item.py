# You are on your own... good luck.
from .item import Item

class DigitalItem(Item):
  def __init__(self, name, price):
    super().__init__(name, price)

    # digital items always have a quantity of exactly 1.
    self.quantity = 1

  def sell(self, amount):
    return True

  def stock(self, amount):
    return True
