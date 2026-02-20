# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

#store known values
known_values = {
}

def fibonacci(n):
    if n in known_values:
        return known_values[n]
    

    if n <= 1:
        return n
    else:
        
        result = fibonacci(n - 1) + fibonacci(n - 2)
        
        known_values[n] = result
        
        return result