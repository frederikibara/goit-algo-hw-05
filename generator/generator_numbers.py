import re
from typing import Callable

def generator_numbers(text: str):  
    """
    Takes a string : filters and extracts natural numbers. 
    Returns -> generator
    """
    template = r'\d+\.\d+'
    real_nums = re.findall(template, text)
    
    for num in real_nums:    
        yield float(num)
    

def sum_profit(text: str, func: Callable):
    """ 
    Accepts str and generator function. 
    Returns -> sum of the numbers from input values.
    """
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")