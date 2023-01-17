def even_fibonacci_sum(n):
    base_seq = [0, 1]
    while base_seq[-1] < n:
        base_seq.append(base_seq[-2] + base_seq[-1])
    return base_seq[:-1]


print(sum([i for i in even_fibonacci_sum(4e6) if i%2 ==0]))

##### TESTS ####

print(even_fibonacci_sum(10))  # should be 44
print(even_fibonacci_sum(15))  # should be 188
print(even_fibonacci_sum(1))   # should be 0



