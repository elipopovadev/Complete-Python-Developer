"""
Created on Fri Jan 14 19:43:31 2022

@author: eli
"""
from datetime import date
import pandas as pd

born_inString = input('What year were you born? ')
born_inDate = pd.to_datetime(born_inString)

def calculate_age(born_inDate):
    today = date.today()
    return today.year - born_inDate.year - ((today.month, today.day) < (born_inDate.month, born_inDate.day))

print(f'You are {calculate_age(born_inDate)} years old.')


