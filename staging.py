import time

# Staging allows us to finish expensive computations early on and reference the
# result as we need it. This allows our code to not have to repeatedly perform the 
# expensive computations. This results in greater efficiency.

def get_10_slowly():
    time.sleep(5) # Waits for 5 seconds
    return 10

def add10():
    y = get_10_slowly() # We do this first, meaning we don't have to call it again in future calls
    return lambda x: x + y

def mul10():
    y = get_10_slowly() # We do this first, meaning we don't have to call it again in future calls
    return lambda x: x * y

if __name__ == '__main__':
    print("Doing the slow functions...")
    # Process should take 10 seconds total
    add = add10()
    mult = mul10()
    print("Done with the slow functions...")

    time.sleep(3)
    print("Now, let me do the computations...\n")

    print(add(10)) # Results in 20
    print(add(12)) # Results in 22
    print(mult(11)) # Results in 110
    print(mult(111)) # Results in 1110
