from typing import Callable
import re
from decimal import Decimal

def generator_numbers(text: str):

    pattern = r' \d+\.\d+ '

    for n in re.findall(pattern, text):
        yield float(n)

def sum_profit(text: str, func: Callable):
    
    income = 0.0

    for i in func(text):

        income += i

    return Decimal(str(income)).quantize(Decimal('0.00'))

text = "Загальний дохід працівника складається з декількох частин:\
     0.10 як основний дохід, доповнений додатковими надходженнями\
     1000.20 і 0.01 доларів 0.1 0.0 . "

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")