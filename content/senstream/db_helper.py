import mysql.connector
import numpy as np
import pandas as pd

class Helper:
  def __init__(self,name):
    self.name = name
    print("The helper has been created")

  def connect(self):
    cnx = mysql.connector.connect(user="tom",password="Manhattan44joke#",host="resensys.net",port=3306)
    query = "SELECT * FROM admin.Accounts;"
    c = cnx.cursor()
    c.execute(query)
    results = c.fetchall()

    cnx.close()
    print("results: ",results)

  def test1(self,message):
    print(f"The helper printed message: {message}")

  def test2(self):
    print(f"The name of the helper is {self.name}")
