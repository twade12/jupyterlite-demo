import numpy as np
import pandas as pd

class Helper:
  def __init__(self,name):
    self.name = name
    print("The helper has been created")

  def test1(self,message):
    print(f"The helper printed message: {message}")

  def test2(self):
    print(f"The name of the helper is {self.name}")
