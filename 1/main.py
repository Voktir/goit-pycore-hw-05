from functools import lru_cache

def caching_fibonacci():

    cache = {0 : 0, 1 : 1} # Якщо {} - немає перших двох значень, стовримо нижче

    @lru_cache(None) # Ще тохи кешування для оптимізації обчислень

    def fibonacci(n) -> int:
        if n < 0:
            return "Incorrect Fibonacci key"
        
        # Якщо cache = {}
        # elif n < 2:
        #     return n

        elif n in cache:
            return cache[n]

        # Можливо й так, замість elif n in cache:
        # elif n < len(cache):
        #     return cache[n]        
        
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            # print(f"fibonacci cache[{n}] = {cache[n]} -> {cache}")
            return cache[n]

    return fibonacci

fib = caching_fibonacci()

# # Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
# print(fib(15)) # Виведе 610
# print(fib(10)) # Виведе 55
# print(fib(-1))
# print(fib(16)) # Виведе 987
