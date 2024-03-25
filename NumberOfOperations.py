import math


def convert_to_time(operations):
    seconds = operations / 10**9
    hours = seconds / 3600
    days = hours / 24
    years = days / 365.25
    return seconds, hours, days, years

    
N = 2**2000
try:
    logn = math.log(N)
    loglogn = math.log(logn)
    prod = logn * loglogn
    sqrtprod = math.sqrt(prod)
    print(f"The result of the expression is: {convert_to_time(math.exp(sqrtprod))}\n\n")
except ValueError as e:
    print(e)
