from typing import Callable
import re

def generator_numbers(text: str):

    pattern = r' \d+\.\d+ '
    
    i = re.findall(pattern, text)    

    print(i)

    for n in i:
        yield float(n)

def sum_profit(text: str, func: Callable):
    
    income = 0.0

    for i in func(text):

        income += i
        print(i)


    return income

text = "Загальний дохід працівника складається з декількох частин:\
     1000.01 як основний дохід, доповнений додатковими надходженнями\
     27.45 і \
     324.00 доларів . "

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")

