n_terms = 10
fibonacci_sequence = [0, 1]

for i in range(n_terms):
    next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_term)

print(fibonacci_sequence)
