class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Return the next value in the sequence"""
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Create a countdown from 5
countdown = Countdown(5)

# Use in a for loop
print("Counting down from 5:")
for number in countdown:
    print(number)
# Output:
# 5
# 4
# 3
# 2
# 1
# 0

# Create another countdown
print("\nCounting down from 3:")
for number in Countdown(3):
    print(number)
# Output:
# 3
# 2
# 1
# 0

# Try to iterate again (will not work as iterator is exhausted)
print("\nTrying to iterate again:")
try:
    for number in countdown:
        print(number)
except StopIteration:
    print("Iterator is exhausted")

"""
Explanation:
1. Iterator Protocol requires:
   - __iter__() method to return the iterator object
   - __next__() method to return the next value
   - StopIteration exception to signal the end

2. Countdown class:
   - Stores the start value
   - Tracks current value
   - Decrements on each iteration
   - Stops at 0

3. Features:
   - Can be used in for loops
   - Can be used with list()
   - Can be used with next()
   - Exhausts after one full iteration
"""
