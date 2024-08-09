n_terms = 10
fibonacci_series = [0, 1]

for i in range(n_terms):
    next_term = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_term)

print(fibonacci_series)
