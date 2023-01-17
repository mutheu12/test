def fibonacci(ix):
    """Function to return the Fibonacci number at the specified index."""

    # Base case is 0 or 1, at indexes 0, 1 and 2
    if ix == 0:
        return 0
    elif ix == 1 or ix == 2:
        return 1
    else:
        return fibonacci(ix - 1) + fibonacci(ix - 2)


def even_fibonacci_sum(limit):
    """Function to calculate the sum of even numbers in the Fibonacci sequence up to the limit."""

    even_sum = 0

    for i in range(limit):
        number = fibonacci(i)

        # If the remainder is zero when divided by 2, then it is even
        if number % 2 == 0:
            even_sum += number

    return even_sum


##### TESTS ####

# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0


def is_valid_subsequence(array, sequence):

    # If the length of the subsequence is longer than the array, it cannot be a subsequence
    if len(sequence) > len(array):
        return False

    counter = 0
    for num in array:
        if num == sequence[counter]:
            counter += 1

            # If the counter is now equal to the length of the sequence, all items found, return True
            if counter == len(sequence):
                return True

    # If after looping through the counter is less than the length of the sequence, return False
    if counter < len(sequence):
        return False


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

# print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

# print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

# print(is_valid_subsequence(array3, sequence3))  # TRUE



