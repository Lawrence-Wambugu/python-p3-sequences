def print_fibonacci(length):
    # Handle edge cases for length 0 or 1
    if length == 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence for length > 2
    for i in range(2, length):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(fib_sequence)
